"""七年级下·实数运算。区分定义域和根式符号，保留 RealNumberOperations 入口。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
ADD = BLUE_C
MUL = GREEN_C
KEY = YELLOW
WARN = ORANGE


class RealNumberOperations(Scene):
    def fit(self, mob, max_width=7.5):
        if mob.width > max_width:
            mob.scale_to_fit_width(max_width)
        return mob

    def heading(self, text):
        mob = self.fit(Text(text, font_size=39, color=GOLD)).move_to(UP * 5.8)
        self.play(Write(mob), run_time=0.65)
        return mob

    def formula(self, tex, y, color=WHITE, size=36):
        mob = self.fit(MathTex(tex, font_size=size, color=color)).move_to(UP * y)
        self.play(Write(mob), run_time=0.65)
        return mob

    def note(self, text, y, color=WHITE, size=26):
        mob = self.fit(Text(text, font_size=size, color=color)).move_to(UP * y)
        self.play(FadeIn(mob), run_time=0.5)
        return mob

    def clear_stage(self):
        visible = [mob for mob in self.mobjects if mob is not self.author]
        if visible:
            self.play(FadeOut(VGroup(*visible)), run_time=0.45)

    def construct(self):
        self.camera.background_color = BG
        self.author = self.fit(
            Text("上海初高中数学直通车 @emptyandcalm", font_size=18, color=GRAY_B)
        ).move_to(UP * 6.75)
        self.add(self.author)
        self.scene_opening()
        self.scene_add_sub()
        self.scene_mul_div()
        self.scene_simplify()
        self.scene_abs_value()
        self.scene_laws()
        self.scene_combined()
        self.scene_outro()

    def scene_opening(self):
        self.heading("根号里的数，也能参与运算")
        # 对角线精确由所画正方形的两个角连接；边长画面单位仅供示意。
        square = Square(side_length=2.4, color=ADD, fill_opacity=0.12).move_to(UP * 1.8)
        diagonal = Line(square.get_corner(DL), square.get_corner(UR), color=KEY)
        self.play(Create(square), Create(diagonal), run_time=1.0)
        self.note("设正方形的边长为 1", 0.15, ADD, 23)
        self.formula(r"d^2=1^2+1^2=2", -0.8, ADD)
        self.formula(r"d=\sqrt{2}", -2.0, KEY)
        self.note("图形与根式对应，运算必须遵守条件", -3.2)
        self.wait(0.8)
        self.clear_stage()

    def scene_add_sub(self):
        self.heading("加减：先化简，再合并同类项")
        self.formula(r"\sqrt{2}+\sqrt{8}", 3.9, ADD)
        self.formula(r"=\sqrt{2}+2\sqrt{2}", 2.5, ADD)
        self.formula(r"=3\sqrt{2}", 1.1, KEY)
        self.note("根号内不同，不一定不能合并：先试着化简", -0.35)
        self.formula(r"\sqrt{2}+\sqrt{3}", -1.7, WARN)
        self.note("根号 2 与根号 3 化简后仍不是同类项", -2.85, WARN)
        self.wait(1.0)
        self.clear_stage()

    def scene_mul_div(self):
        self.heading("乘除：先确认被开方数的范围")
        self.formula(r"\sqrt{a}\sqrt{b}=\sqrt{ab}", 4.2, MUL)
        self.note("条件：a 和 b 都不小于 0", 3.3, KEY, 24)
        self.formula(r"\frac{\sqrt{a}}{\sqrt{b}}=\sqrt{\frac{a}{b}}", 1.8, MUL)
        self.note("除法还要求 b 大于 0，分母不能为 0", 0.8, KEY, 24)
        self.formula(r"\sqrt{2}\sqrt{3}=\sqrt{6}", -0.8, MUL)
        self.formula(r"\frac{\sqrt{12}}{\sqrt{3}}=2", -2.0, MUL)
        self.wait(1.0)
        self.clear_stage()

    def scene_simplify(self):
        self.heading("化简根式：平方数提出根号")
        self.formula(r"\sqrt{8}=\sqrt{4\times2}=2\sqrt{2}", 3.8, ADD, 34)
        self.formula(r"\sqrt{18}=\sqrt{9\times2}=3\sqrt{2}", 2.1, ADD, 34)
        self.formula(r"\sqrt{a^2b}=|a|\sqrt{b}", 0.4, KEY, 36)
        self.note("条件：a 为实数，b 不小于 0", -0.75, KEY)
        self.formula(r"\sqrt{(-3)^2\times2}=3\sqrt{2}", -2.1, WARN, 32)
        self.note("负数因子提出根号时，要用绝对值", -3.25, WARN, 24)
        self.wait(1.0)
        self.clear_stage()

    def scene_abs_value(self):
        self.heading("绝对值：先判断括号内的符号")
        self.formula(r"|\sqrt{2}-1|=\sqrt{2}-1", 3.9, ADD, 34)
        self.note("因为 2 大于 1，所以根号 2 大于 1", 2.8)
        self.formula(r"|3-\sqrt{10}|=\sqrt{10}-3", 1.25, WARN, 34)
        self.note("因为 10 大于 9，所以根号 10 大于 3", 0.1)
        self.formula(r"|-\sqrt{5}|=\sqrt{5}", -1.3, KEY)
        self.note("绝对值总是非负的", -2.7, KEY)
        self.wait(1.0)
        self.clear_stage()

    def scene_laws(self):
        self.heading("运算律仍然成立")
        formulas = (
            r"a+b=b+a",
            r"(a+b)+c=a+(b+c)",
            r"ab=ba",
            r"a(b+c)=ab+ac",
        )
        for i, tex in enumerate(formulas):
            self.formula(tex, 4.1 - i * 1.7, ADD if i < 2 else MUL, 33)
        self.note("a、b、c 为实数；含分母、根号时仍须满足定义域", -3.1, KEY, 23)
        self.wait(1.0)
        self.clear_stage()

    def scene_combined(self):
        self.heading("综合例题：先化简后运算")
        self.formula(r"(\sqrt{3}+\sqrt{2})(\sqrt{3}-\sqrt{2})", 3.9, ADD, 34)
        self.formula(r"=(\sqrt{3})^2-(\sqrt{2})^2=1", 2.4, KEY, 34)
        self.formula(r"\sqrt{2}\sqrt{8}+\sqrt{3}\sqrt{3}", 0.65, MUL, 34)
        self.formula(r"=\sqrt{16}+3=7", -0.85, KEY, 34)
        self.note("先判断运算是否合法，再代入并化简", -2.4)
        self.wait(1.0)
        self.clear_stage()

    def scene_outro(self):
        self.heading("本课总结")
        self.note("加减：先化简，再合并同类项", 3.9, ADD)
        self.note("乘除：非负被开方数，分母还需非零", 2.4, MUL)
        self.formula(r"\sqrt{a^2b}=|a|\sqrt{b}\quad(b\geq0)", 0.5, KEY, 30)
        self.note("不要漏掉绝对值与定义域", -1.1, WARN)
        self.wait(1.8)

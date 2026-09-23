"""A-Level P1 / 1.1: solving quadratic equations by factorisation.

Original vertical (9:16) Chinese/English visual lesson, ~90-120 seconds depending
on render speed. Requires Manim Community, LaTeX, and a Chinese system font.
This module does not set pixel_width or pixel_height: CLI controls resolution.

Render (from this directory):
    python -m manim render -r 270,480 --fps 15 lesson.py P1Factorisation
    python -m manim render -r 1080,1920 --fps 30 lesson.py P1Factorisation

Content is an original worked example using x^2-5x+6=0, NOT a reproduction
of an exercise or worked example printed in the textbook.
"""
from manim import *
from math_model import (expand_linear_factors, solve_monic_by_integer_factors,
                        square_partition, f)

# Manim Community expects 9 x 16 logical units for this portrait lesson.
config.frame_width = 9
config.frame_height = 16

BG = '#101724'
PANEL = '#1C293A'
INK = '#EAF1FA'
MUTED = '#9BB2CB'
TEAL = '#49D9D0'
GOLD = '#FFD16A'
CORAL = '#FF7D86'
GREEN = '#7FE3A7'
FONT = 'Noto Sans CJK SC'  # change to an installed font if necessary


def cn(s, size=29, color=INK, **kwargs):
    obj = Text(s, font=FONT, font_size=size, color=color, **kwargs)
    if obj.width > 7.65:
        obj.scale_to_fit_width(7.65)
    return obj


def eq(s, size=41, color=INK):
    return MathTex(s, font_size=size, color=color)


def panel(width=7.75, height=2.3):
    return RoundedRectangle(corner_radius=.18, width=width, height=height,
                            fill_color=PANEL, fill_opacity=.97,
                            stroke_color='#36516A', stroke_width=1.5)


def note(caption, at=-4.85, size=24, color=MUTED):
    label=cn(caption, size=size, color=color)
    label.move_to((0,at,0))
    return label


def rect_of(left, right, bottom, top, fill, opacity=.60, stroke=INK, width=1.5):
    m=Rectangle(width=right-left, height=top-bottom,
                fill_color=fill, fill_opacity=opacity,
                stroke_color=stroke, stroke_width=width)
    m.move_to(((left+right)/2,(bottom+top)/2,0))
    return m


def assert_visible(scene, ids):
    """Lightweight *actual-Mobject* checkpoint (not a per-frame visual audit).

    A visible object may be inside one of the Scene's top-level VGroups.
    Limits are this project's portrait conservative safe region.
    """
    def descendants(obj):
        yield obj
        for child in obj.submobjects:
            yield from descendants(child)
    visible={id(m) for root in scene.mobjects for m in descendants(root)}
    for object_id, mob in ids.items():
        if id(mob) not in visible:
            raise AssertionError(f'{object_id}: not in actual Scene family')
        # Individual glyphs need not be registered; complete text/math bbox is.
        if mob.get_left()[0] < -4.04 or mob.get_right()[0] > 4.04:
            raise AssertionError(f'{object_id}: horizontal safe-area breach')
        if mob.get_bottom()[1] < -7.04 or mob.get_top()[1] > 7.04:
            raise AssertionError(f'{object_id}: vertical safe-area breach')


class P1Factorisation(Scene):
    """One self-contained lesson; narration-free with paced on-screen captions."""

    def construct(self):
        self.camera.background_color=BG
        assert expand_linear_factors(1,-2,1,-3) == (1,-5,6)
        assert solve_monic_by_integer_factors(-5,6) == (2,3)
        self.make_chrome()
        self.opening()
        self.algebra_tiles()
        self.finding_pair()
        self.zero_product()
        self.branches()
        self.parabola()
        self.common_trap()
        self.practice()
        self.conclusion()

    def make_chrome(self):
        logo=cn('A-Level', size=30, color=BG, weight="BOLD")
        pill=RoundedRectangle(corner_radius=.16, width=1.77, height=.57,
                              fill_color=TEAL, fill_opacity=1, stroke_width=0)
        logo.move_to(pill)
        p1=cn('PURE MATHEMATICS 1  ·  P1', size=21, color=INK)
        p1.next_to(pill, RIGHT, buff=.18)
        self.header=VGroup(pill,logo,p1)
        self.header.move_to((-.10,6.62,0))
        rule=Line((-3.82,6.18,0),(3.82,6.18,0),stroke_color='#36516A')
        foot=cn('CHAPTER 1  /  1.1  FACTORISATION',size=18,color=MUTED)
        foot.move_to((0,-6.57,0))
        self.chrome=VGroup(self.header,rule,foot)
        self.add(self.chrome)
        assert_visible(self,{'course_brand':self.header,'chapter_footer':foot})

    def clear_content(self):
        for mob in list(self.mobjects):
            if mob is not self.chrome:
                self.play(FadeOut(mob),run_time=.32)

    def heading(self, title, subtitle=None):
        h=cn(title,34,INK).move_to((0,5.37,0))
        self.play(FadeIn(h,shift=.13*DOWN),run_time=.45)
        if subtitle:
            sub=cn(subtitle,21,MUTED).move_to((0,4.84,0))
            self.play(FadeIn(sub),run_time=.25)
            return h,sub
        return h

    def opening(self):
        self.heading('如何把二次方程拆成两条一次方程？',
                     'Solving quadratic equations by factorisation')
        question=eq(r'x^2-5x+6=0',56).move_to((0,2.45,0))
        line=Line((-3.14,1.81,0),(3.14,1.81,0),color=TEAL,stroke_width=3)
        chips=VGroup(cn('因式分解',27,TEAL),cn('零乘积法则',27,GOLD),cn('检验根',27,GREEN))
        chips.arrange(RIGHT,buff=.3).move_to((0,.44,0))
        p=panel(height=2.0).move_to((0,-1.65,0))
        prompt=cn('一个乘积等于 0，意味着什么？',29).move_to(p.get_center())
        self.play(Write(question),Create(line),run_time=1.2)
        self.play(LaggedStart(*[FadeIn(c,shift=.2*UP) for c in chips],lag_ratio=.25),run_time=1.2)
        self.play(FadeIn(p),FadeIn(prompt),run_time=.65)
        self.wait(1.6)
        assert_visible(self,{'question':question,'brand':self.header,'prompt':prompt})
        self.clear_content()

    def algebra_tiles(self):
        self.heading('第一步：先看因式从哪里来', '面积模型只用于直观解释；图中取 x = 5')
        # 5x5 diagram: right strip width 2, upper strip height 3.
        # For x>=3 only, central remainder: (x-2)*(x-3).
        data=square_partition(5)
        assert data['square']-data['right_strip']-data['upper_strip']+data['overlap']==6
        side=.72; left=-1.80; bottom=-1.65; right=left+5*side; top=bottom+5*side
        split_x=left+3*side; split_y=bottom+2*side
        whole=rect_of(left,right,bottom,top,TEAL,.12,TEAL,2.5)
        upper=rect_of(left,right,split_y,top,GOLD,.38,GOLD,1.5)
        right_strip=rect_of(split_x,right,bottom,top,CORAL,.35,CORAL,1.5)
        overlap=rect_of(split_x,right,split_y,top,GOLD,.83,GOLD,2)
        remain=rect_of(left,split_x,bottom,split_y,GREEN,.55,GREEN,2.5)
        labs=VGroup(
            eq('x=5',27).next_to(whole,UP,buff=.22),
            eq('x-2=3',28,GREEN).next_to(remain,DOWN,buff=.16),
            eq('x-3=2',27,GREEN).next_to(remain,LEFT,buff=.17),
            eq('2',27,CORAL).move_to(((right+split_x)/2,bottom-.30,0)),
            eq('3',27,GOLD).move_to((right+.32,(split_y+top)/2,0)))
        for obj in [whole,upper,right_strip,overlap,remain]:
            self.play(FadeIn(obj),run_time=.42)
        self.play(FadeIn(labs),run_time=.45)
        frm=eq(r'5^2-2(5)-3(5)+2\cdot3=6',33)
        frm.move_to((0,-3.24,0))
        statement=eq(r'x^2-5x+6=(x-2)(x-3)',38)
        statement.move_to((0,-4.19,0))
        note_text=note('重叠区域被减了两次，必须加回一次。',at=-5.20,size=22)
        self.play(Write(frm),run_time=1.2)
        self.play(Write(statement),FadeIn(note_text),run_time=1.2)
        self.wait(1.7)
        assert_visible(self,{'area_diagram':whole,'remaining_area':remain,'identity':statement})
        self.clear_content()

    def finding_pair(self):
        self.heading('代数方法：寻找两个合适的数', '乘积等于常数项；和等于一次项系数')
        problem=eq(r'x^2-5x+6',49).move_to((0,3.58,0))
        p_left=panel(width=3.5,height=2.26).move_to((-1.94,.74,0))
        p_right=panel(width=3.5,height=2.26).move_to((1.94,.74,0))
        sums=VGroup(cn('和是 -5',26,TEAL),eq(r'-2+(-3)=-5',33,TEAL))
        prod=VGroup(cn('积是 +6',26,GOLD),eq(r'(-2)(-3)=6',33,GOLD))
        sums.arrange(DOWN,buff=.3).move_to(p_left)
        prod.arrange(DOWN,buff=.3).move_to(p_right)
        result=eq(r'(x-2)(x-3)',49,GREEN).move_to((0,-2.40,0))
        arrow=Arrow((0,-.67,0),(0,-1.72,0),color=GREEN,buff=.10,stroke_width=4)
        verify=eq(r'x^2-3x-2x+6=x^2-5x+6',34).move_to((0,-4.00,0))
        caption=note('验证：把括号乘开，必须回到原来的三项式。',at=-5.12,size=22)
        self.play(Write(problem),run_time=.65)
        self.play(FadeIn(p_left),FadeIn(p_right),run_time=.55)
        self.play(Write(sums),Write(prod),run_time=1.4)
        self.play(Create(arrow),Write(result),run_time=1.0)
        self.play(Write(verify),FadeIn(caption),run_time=1.2)
        self.wait(1.6)
        assert_visible(self,{'sum_pair':sums,'product_pair':prod,'candidate_factors':result,'expansion':verify})
        self.clear_content()

    def zero_product(self):
        self.heading('第二步：利用零乘积法则', 'If A · B = 0, then A = 0 or B = 0')
        orig=eq(r'x^2-5x+6=0',52).move_to((0,3.55,0))
        factors=eq(r'(x-2)(x-3)=0',51).move_to((0,1.80,0))
        down=Arrow((0,3.04,0),(0,2.35,0),buff=0,stroke_width=4,color=TEAL)
        a=eq('A',42,TEAL).move_to((-1.20,.45,0))
        b=eq('B',42,GOLD).move_to((1.20,.45,0))
        mult=eq(r'A\cdot B=0',42).move_to((0,-.57,0))
        branches=VGroup(eq('A=0',39,TEAL),cn('或',27,MUTED),eq('B=0',39,GOLD))
        branches.arrange(RIGHT,buff=.42).move_to((0,-2.05,0))
        explanation=note('若两个实数的乘积为 0，至少一个因子必须是 0。',at=-4.08,size=22)
        self.play(Write(orig),run_time=.7)
        self.play(Create(down),Write(factors),run_time=1.05)
        self.play(FadeIn(a),FadeIn(b),Write(mult),run_time=.8)
        self.play(FadeIn(branches,shift=.18*UP),FadeIn(explanation),run_time=.7)
        self.wait(1.8)
        assert_visible(self,{'factors':factors,'zero_product':branches})
        self.clear_content()

    def branches(self):
        self.heading('第三步：分别令每个因子为 0')
        top=eq(r'(x-2)(x-3)=0',53).move_to((0,3.58,0))
        left_panel=panel(width=3.65,height=2.48).move_to((-1.97,.65,0))
        right_panel=panel(width=3.65,height=2.48).move_to((1.97,.65,0))
        left_text=VGroup(eq('x-2=0',40,TEAL),eq('x=2',46,GREEN)).arrange(DOWN,buff=.40).move_to(left_panel)
        right_text=VGroup(eq('x-3=0',40,GOLD),eq('x=3',46,GREEN)).arrange(DOWN,buff=.40).move_to(right_panel)
        stem=Line((0,3.05,0),(0,2.45,0),color=INK)
        fork=VGroup(Line((0,2.45,0),(-1.97,1.97,0),color=TEAL),
                    Line((0,2.45,0),(1.97,1.97,0),color=GOLD))
        answer_bg=panel(height=1.20).move_to((0,-2.37,0))
        answer=eq(r'\boxed{x=2\quad\mathrm{or}\quad x=3}',43,GREEN).move_to(answer_bg)
        self.play(Write(top),Create(stem),Create(fork),run_time=1.1)
        self.play(FadeIn(left_panel),Write(left_text),run_time=1.0)
        self.play(FadeIn(right_panel),Write(right_text),run_time=1.0)
        self.play(FadeIn(answer_bg),Write(answer),run_time=1.2)
        self.play(FadeIn(note('两条分支都要保留：题目问的是全部实数解。',at=-4.25,size=23)))
        self.wait(2)
        assert_visible(self,{'left_branch':left_panel,'right_branch':right_panel,'solution':answer})
        self.clear_content()

    def parabola(self):
        self.heading('第四步：图像让两个解看得见', '方程 f(x)=0 对应曲线与 x 轴的交点')
        ax=Axes(x_range=[0,5.5,1],y_range=[-1,7,1],
                x_length=6.5,y_length=3.8,
                axis_config={'color':MUTED,'include_numbers':False,'stroke_width':1.5},
                tips=False).move_to((0,.52,0))
        curve=ax.plot(f,x_range=[0,5],color=TEAL,stroke_width=5)
        roots=(2,3)
        dots=VGroup(*[Dot(ax.c2p(root,0),radius=.10,color=GREEN) for root in roots])
        for r in roots:
            assert f(r)==0
        # Roots positioned with the actual axes coordinate transform.
        root_tags=VGroup(*[eq(f'x={r}',30,GREEN).move_to(ax.c2p(r,-.78)+DOWN*.36) for r in roots])
        center_dot=Dot(ax.c2p(2.5,-.25),radius=.065,color=GOLD)
        axis_x=eq('x',25,MUTED).next_to(ax.x_axis,RIGHT,buff=.11)
        axis_y=eq('y',25,MUTED).next_to(ax.y_axis,UP,buff=.11)
        formula=eq(r'y=(x-2)(x-3)',41).move_to((0,-3.25,0))
        desc=note('在 x=2 和 x=3 处，函数值恰好为 0。',at=-4.37,size=24)
        self.play(Create(ax),Write(axis_x),Write(axis_y),run_time=1.15)
        self.play(Create(curve),run_time=1.55)
        self.play(FadeIn(dots,scale=1.4),FadeIn(root_tags),FadeIn(center_dot),run_time=.9)
        self.play(Write(formula),FadeIn(desc),run_time=.8)
        self.wait(2)
        assert_visible(self,{'axes':ax,'graph':curve,'root_markers':dots,'graph_formula':formula})
        self.clear_content()

    def common_trap(self):
        self.heading('避坑：不能随意除掉一个含 x 的因子')
        question=eq(r'(x-2)(x-3)=0',49).move_to((0,3.22,0))
        wrong=eq(r'(x-3)=0',46,CORAL).move_to((0,1.68,0))
        false_label=cn('错误地约去 (x−2)',25,CORAL).move_to((0,2.38,0))
        warning=cn('除以 (x−2) 会漏掉 x=2！',31,CORAL).move_to((0,.18,0))
        proof=eq(r'(2-2)(2-3)=0',42,GREEN).move_to((0,-1.57,0))
        statement=note('因子可能等于 0 时，不能直接除去它。',at=-3.22,size=25)
        self.play(Write(question),run_time=.75)
        self.play(FadeIn(false_label),Write(wrong),run_time=.85)
        self.play(FadeIn(warning),Write(proof),run_time=1.1)
        self.play(FadeIn(statement),run_time=.6)
        self.wait(1.9)
        assert_visible(self,{'avoid_cancel':warning,'counterexample':proof})
        self.clear_content()

    def practice(self):
        self.heading('试一试：先提取公因子，再分解', '练习题（原创）：与基础示例同一种思路')
        problem=eq(r'2x^2-10x+12=0',48).move_to((0,3.45,0))
        step1=eq(r'2(x^2-5x+6)=0',42).move_to((0,2.00,0))
        step2=eq(r'2(x-2)(x-3)=0',43).move_to((0,.45,0))
        step3=eq(r'\boxed{x=2\quad\mathrm{or}\quad x=3}',42,GREEN).move_to((0,-1.35,0))
        hint=note('先暂停思考：可否将各项的公因子 2 提取出来？',at=-4.10,size=21)
        self.play(Write(problem),FadeIn(hint),run_time=1.0)
        self.wait(2.0)
        self.play(Write(step1),run_time=.95)
        self.play(Write(step2),run_time=.95)
        self.play(Write(step3),run_time=.95)
        self.wait(1.5)
        assert_visible(self,{'practice_answer':step3})
        self.clear_content()

    def conclusion(self):
        self.heading('本节回顾：三步求解，一步检验', 'A-Level  ·  Pure Mathematics 1  ·  1.1')
        card=panel(height=4.65).move_to((0,.6,0))
        lines=VGroup(
            cn('① 整理成“多项式 = 0”',28,INK),
            eq(r'x^2-5x+6=0',40),
            cn('② 分解为两个一次因子的乘积',28,INK),
            eq(r'(x-2)(x-3)=0',40,TEAL),
            cn('③ 用零乘积法则，分别令因子为 0',26,INK),
            eq(r'\boxed{x=2\quad\mathrm{or}\quad x=3}',39,GREEN),
        ).arrange(DOWN,buff=.24).move_to(card)
        check=eq(r'f(2)=0\,,\qquad f(3)=0',37,GOLD).move_to((0,-3.42,0))
        closing=note('关键：两个因子都检查，不要漏解。',at=-4.65,size=24)
        self.play(FadeIn(card),LaggedStart(*[FadeIn(m,shift=.08*UP) for m in lines],lag_ratio=.16),run_time=3.1)
        self.play(Write(check),FadeIn(closing),run_time=1.0)
        self.wait(2.5)
        assert_visible(self,{'closing_card':card,'final_result':lines[-1],'verified_roots':check})

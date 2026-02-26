from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class ParallelLineDetermination(Scene):
    """
    平行线的判定教学动画场景
    
    三种判定方法:
    1. 同位角相等 ⟹ 两直线平行
    2. 内错角相等 ⟹ 两直线平行  
    3. 同旁内角互补 ⟹ 两直线平行
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 平行线
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 截线
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 角度标识
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线和标注
        self.COLOR_TEXT = WHITE             # 白色 - 文字
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_corresponding_angles()
        self.show_alternate_angles()
        self.show_co_interior_angles()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化平行线和截线的所有几何元素"""
        # 基准参数
        self.SCALE = 1.0
        self.OFFSET = UP * 0.5
        
        # 定义两条平行线 (水平方向，y坐标差固定)
        # 平行线1: y = 2
        self.l1_start = np.array([-4, 2, 0]) * self.SCALE + self.OFFSET
        self.l1_end = np.array([4, 2, 0]) * self.SCALE + self.OFFSET
        
        # 平行线2: y = -2 (与线1垂直距离为4)
        self.l2_start = np.array([-4, -2, 0]) * self.SCALE + self.OFFSET
        self.l2_end = np.array([4, -2, 0]) * self.SCALE + self.OFFSET
        
        # 截线 (从左上到右下斜穿两条平行线)
        self.t_start = np.array([-1, 4, 0]) * self.SCALE + self.OFFSET
        self.t_end = np.array([1, -4, 0]) * self.SCALE + self.OFFSET
        
        # 计算截线与平行线的交点
        # 对于水平线 y = c 和任意线段，交点可通过线性插值计算
        # 平行线1: y = self.l1_start[1]
        # 平行线2: y = self.l2_start[1]
        
        # 交点1: 截线与平行线1的交点
        # 直线方程: 截线上的点 P = t_start + t*(t_end - t_start)
        # 当 Py = l1_y 时求解 t
        t_param1 = (self.l1_start[1] - self.t_start[1]) / (self.t_end[1] - self.t_start[1])
        self.intersection1 = self.t_start + t_param1 * (self.t_end - self.t_start)
        
        # 交点2: 截线与平行线2的交点
        t_param2 = (self.l2_start[1] - self.t_start[1]) / (self.t_end[1] - self.t_start[1])
        self.intersection2 = self.t_start + t_param2 * (self.t_end - self.t_start)
        
        # 为了后续角度计算，定义一些参考点
        # 在平行线1上，交点左右各取一点
        self.point_on_l1_left = self.intersection1 + np.array([-0.8, 0, 0])
        self.point_on_l1_right = self.intersection1 + np.array([0.8, 0, 0])
        
        # 在平行线2上，交点左右各取一点
        self.point_on_l2_left = self.intersection2 + np.array([-0.8, 0, 0])
        self.point_on_l2_right = self.intersection2 + np.array([0.8, 0, 0])
        
        # 在截线上，交点上下各取一点
        self.point_on_t_above_i1 = self.intersection1 + (self.t_end - self.t_start) * 0.3
        self.point_on_t_below_i1 = self.intersection1 - (self.t_end - self.t_start) * 0.3
        self.point_on_t_above_i2 = self.intersection2 + (self.t_end - self.t_start) * 0.3
        self.point_on_t_below_i2 = self.intersection2 - (self.t_end - self.t_start) * 0.3
        
        # 验证几何计算
        self.verify_geometry()
        
        # 创建几何对象
        self.parallel_line1 = Line(self.l1_start, self.l1_end, color=self.COLOR_PRIMARY, stroke_width=4)
        self.parallel_line2 = Line(self.l2_start, self.l2_end, color=self.COLOR_PRIMARY, stroke_width=4)
        self.transversal = Line(self.t_start, self.t_end, color=self.COLOR_SECONDARY, stroke_width=4)
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证两条线确实是平行的 (y坐标差恒定)
        y_diff_1 = self.l1_start[1] - self.l2_start[1]
        y_diff_2 = self.l1_end[1] - self.l2_end[1]
        
        if abs(y_diff_1 - y_diff_2) > epsilon:
            print(f"ERROR: 两条线不是平行的! y差值: {y_diff_1} vs {y_diff_2}")
        
        # 验证交点确实在对应的线上
        # 交点1应在平行线1上 (y坐标应等于l1的y坐标)
        if abs(self.intersection1[1] - self.l1_start[1]) > epsilon:
            print(f"ERROR: 交点1不在平行线1上! y={self.intersection1[1]} vs {self.l1_start[1]}")
        
        # 交点2应在平行线2上 (y坐标应等于l2的y坐标)
        if abs(self.intersection2[1] - self.l2_start[1]) > epsilon:
            print(f"ERROR: 交点2不在平行线2上! y={self.intersection2[1]} vs {self.l2_start[1]}")
        
        # 验证截线确实穿过两平行线
        # intersection1 和 intersection2 的y坐标应该分别是平行线的y坐标
        if abs(self.intersection1[1] - 2.5) < epsilon or abs(self.intersection2[1] - (-1.5)) < epsilon:  # 根据实际偏移调整
            print("INFO: 截线正确穿过两平行线")
        
        print("✓ 几何验证完成")
    
    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 标题
        title = Text(
            "平行线的判定",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 6)
        
        subtitle = Text(
            "由角的关系推断线的关系",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 绘制两条平行线
        self.play(Create(self.parallel_line1), run_time=1.0)
        self.play(Create(self.parallel_line2), run_time=1.0)
        
        # 绘制截线
        self.play(Create(self.transversal), run_time=1.0)
        
        # 提示文字
        hint = Text(
            "一条截线穿过两条平行线会形成哪些特殊角？",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(hint),
            run_time=0.5
        )
    
    def show_corresponding_angles(self):
        """场景2: 同位角相等判定"""
        # 强调截线
        self.play(self.transversal.animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.5)
        
        # 创建第一个同位角：截线与平行线1在右上方形成的角
        # 顶点在intersection1，一边朝右(平行线1方向)，一边朝右下(截线方向)
        angle1 = Angle.from_three_points(
            self.point_on_l1_right,  # 第一条射线上的点（平行线1上右边的点）
            self.intersection1,      # 顶点
            self.point_on_t_below_i1, # 第二条射线上的点（截线上下方的点）
            radius=0.5,
            quadrant=(1, -1),  # 调整象限使角度弧出现在合适位置
            color=self.COLOR_HIGHLIGHT
        )
        
        # 创建第二个同位角：截线与平行线2在右上方形成的角
        angle2 = Angle.from_three_points(
            self.point_on_l2_right,  # 第一条射线上的点（平行线2上右边的点）
            self.intersection2,      # 顶点
            self.point_on_t_below_i2, # 第二条射线上的点（截线上下方的点）
            radius=0.5,
            quadrant=(1, -1),  # 调整象限使角度弧出现在合适位置
            color=self.COLOR_HIGHLIGHT
        )
        
        # 显示角度
        self.play(Create(angle1), run_time=0.8)
        self.play(Create(angle2), run_time=0.8)
        
        # 角度弧线闪烁效果
        self.play(
            angle1.animate.set_fill(self.COLOR_HIGHLIGHT, opacity=0.5),
            angle2.animate.set_fill(self.COLOR_HIGHLIGHT, opacity=0.5),
            run_time=0.3
        )
        self.play(
            angle1.animate.set_fill(self.COLOR_HIGHLIGHT, opacity=0.2),
            angle2.animate.set_fill(self.COLOR_HIGHLIGHT, opacity=0.2),
            run_time=0.3
        )
        
        # 显示角度相等的文字说明
        angle_text1 = MathTex(r"\alpha", color=self.COLOR_HIGHLIGHT, font_size=36).next_to(angle1, UR, buff=0.1)
        angle_text2 = MathTex(r"\alpha", color=self.COLOR_HIGHLIGHT, font_size=36).next_to(angle2, UR, buff=0.1)
        
        self.play(Write(angle_text1), Write(angle_text2), run_time=0.6)
        
        # 强调角度相等
        self.play(
            angle_text1.animate.set_color(YELLOW),
            angle_text2.animate.set_color(YELLOW),
            run_time=0.5
        )
        
        # 显示判定公式
        formula1 = MathTex(r"\text{同位角相等}", r"\Rightarrow", r"\text{两直线平行}", font_size=32)
        formula1.move_to(DOWN * 3.5)
        formula1[0].set_color(self.COLOR_HIGHLIGHT)
        formula1[2].set_color(self.COLOR_PRIMARY)
        
        self.play(Write(formula1), run_time=0.8)
        
        # 高亮平行线
        self.play(
            self.parallel_line1.animate.set_color(GREEN),
            self.parallel_line2.animate.set_color(GREEN),
            run_time=0.8
        )
        
        # 总结文字
        summary1 = Text("即：若同位角相等，则这两条直线平行", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
        summary1.move_to(DOWN * 4.5)
        
        self.play(Write(summary1), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理：隐藏当前角度相关元素
        self.play(
            FadeOut(angle1),
            FadeOut(angle2), 
            FadeOut(angle_text1),
            FadeOut(angle_text2),
            FadeOut(formula1),
            FadeOut(summary1),
            self.parallel_line1.animate.set_color(self.COLOR_PRIMARY),
            self.parallel_line2.animate.set_color(self.COLOR_PRIMARY),
            run_time=0.8
        )
    
    def show_alternate_angles(self):
        """场景3: 内错角相等判定"""
        # 重新显示基础图形
        self.play(
            Create(self.parallel_line1),
            Create(self.parallel_line2), 
            Create(self.transversal),
            run_time=0.5
        )
        
        # 创建第一个内错角：截线与平行线1在左下方形成的角
        # 顶点在intersection1，一边朝左(平行线1方向)，一边朝右下(截线方向)
        alternate_angle1 = Angle.from_three_points(
            self.point_on_l1_left,  # 第一条射线上的点（平行线1上左边的点）
            self.intersection1,     # 顶点
            self.point_on_t_below_i1, # 第二条射线上的点（截线上下方的点）
            radius=0.5,
            quadrant=(-1, -1),  # 调整象限使角度弧出现在内部
            color=self.COLOR_HIGHLIGHT
        )
        
        # 创建第二个内错角：截线与平行线2在右上方形成的角
        alternate_angle2 = Angle.from_three_points(
            self.point_on_l2_right,  # 第一条射线上的点（平行线2上右边的点）
            self.intersection2,      # 顶点
            self.point_on_t_above_i2, # 第二条射线上的点（截线上方的点）
            radius=0.5,
            quadrant=(1, 1),  # 调整象限使角度弧出现在内部
            color=self.COLOR_HIGHLIGHT
        )
        
        # 显示内错角
        self.play(Create(alternate_angle1), run_time=0.8)
        self.play(Create(alternate_angle2), run_time=0.8)
        
        # 内错角闪烁效果
        self.play(
            alternate_angle1.animate.set_fill(self.COLOR_HIGHLIGHT, opacity=0.5),
            alternate_angle2.animate.set_fill(self.COLOR_HIGHLIGHT, opacity=0.5),
            run_time=0.3
        )
        self.play(
            alternate_angle1.animate.set_fill(self.COLOR_HIGHLIGHT, opacity=0.2),
            alternate_angle2.animate.set_fill(self.COLOR_HIGHLIGHT, opacity=0.2),
            run_time=0.3
        )
        
        # 显示内错角度数
        alt_angle_text1 = MathTex(r"\beta", color=self.COLOR_HIGHLIGHT, font_size=36).next_to(alternate_angle1, DL, buff=0.1)
        alt_angle_text2 = MathTex(r"\beta", color=self.COLOR_HIGHLIGHT, font_size=36).next_to(alternate_angle2, UR, buff=0.1)
        
        self.play(Write(alt_angle_text1), Write(alt_angle_text2), run_time=0.6)
        
        # 强调内错角相等
        self.play(
            alt_angle_text1.animate.set_color(YELLOW),
            alt_angle_text2.animate.set_color(YELLOW),
            run_time=0.5
        )
        
        # 显示判定公式
        formula2 = MathTex(r"\text{内错角相等}", r"\Rightarrow", r"\text{两直线平行}", font_size=32)
        formula2.move_to(DOWN * 3.5)
        formula2[0].set_color(self.COLOR_HIGHLIGHT)
        formula2[2].set_color(self.COLOR_PRIMARY)
        
        self.play(Write(formula2), run_time=0.8)
        
        # 高亮平行线
        self.play(
            self.parallel_line1.animate.set_color(GREEN),
            self.parallel_line2.animate.set_color(GREEN),
            run_time=0.8
        )
        
        # 总结文字
        summary2 = Text("即：若内错角相等，则这两条直线平行", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
        summary2.move_to(DOWN * 4.5)
        
        self.play(Write(summary2), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理：隐藏当前内错角相关元素
        self.play(
            FadeOut(alternate_angle1),
            FadeOut(alternate_angle2),
            FadeOut(alt_angle_text1),
            FadeOut(alt_angle_text2),
            FadeOut(formula2),
            FadeOut(summary2),
            self.parallel_line1.animate.set_color(self.COLOR_PRIMARY),
            self.parallel_line2.animate.set_color(self.COLOR_PRIMARY),
            run_time=0.8
        )
    
    def show_co_interior_angles(self):
        """场景4: 同旁内角互补判定"""
        # 重新显示基础图形
        self.play(
            Create(self.parallel_line1),
            Create(self.parallel_line2),
            Create(self.transversal),
            run_time=0.5
        )
        
        # 创建同旁内角1：截线与平行线1在右下方形成的角
        co_interior_angle1 = Angle.from_three_points(
            self.point_on_l1_right,  # 第一条射线上的点（平行线1上右边的点）
            self.intersection1,      # 顶点
            self.point_on_t_below_i1, # 第二条射线上的点（截线上下方的点）
            radius=0.6,
            quadrant=(1, -1),  # 调整象限使角度弧出现在内部
            color=self.COLOR_HIGHLIGHT
        )
        
        # 创建同旁内角2：截线与平行线2在右上方形成的角（与上面的角在同一侧）
        co_interior_angle2 = Angle.from_three_points(
            self.point_on_l2_right,  # 第一条射线上的点（平行线2上右边的点）
            self.intersection2,      # 顶点
            self.point_on_t_above_i2, # 第二条射线上的点（截线上方的点）
            radius=0.6,
            quadrant=(1, 1),  # 调整象限使角度弧出现在内部
            color=self.COLOR_HIGHLIGHT
        )
        
        # 显示同旁内角
        self.play(Create(co_interior_angle1), run_time=0.8)
        self.play(Create(co_interior_angle2), run_time=0.8)
        
        # 同旁内角闪烁效果
        self.play(
            co_interior_angle1.animate.set_fill(self.COLOR_HIGHLIGHT, opacity=0.5),
            co_interior_angle2.animate.set_fill(self.COLOR_HIGHLIGHT, opacity=0.5),
            run_time=0.3
        )
        self.play(
            co_interior_angle1.animate.set_fill(self.COLOR_HIGHLIGHT, opacity=0.2),
            co_interior_angle2.animate.set_fill(self.COLOR_HIGHLIGHT, opacity=0.2),
            run_time=0.3
        )
        
        # 显示同旁内角度数
        co_int_angle_text1 = MathTex(r"\gamma", color=self.COLOR_HIGHLIGHT, font_size=36).next_to(co_interior_angle1, DR, buff=0.1)
        co_int_angle_text2 = MathTex(r"\delta", color=self.COLOR_HIGHLIGHT, font_size=36).next_to(co_interior_angle2, UR, buff=0.1)
        
        self.play(Write(co_int_angle_text1), Write(co_int_angle_text2), run_time=0.6)
        
        # 计算两角之和（理论上应为180度）
        sum_formula = MathTex(r"\gamma + \delta = 180^\circ", font_size=32).move_to(DOWN * 3)
        sum_formula[0][6:9].set_color(YELLOW)  # 高亮180°
        
        self.play(Write(sum_formula), run_time=0.8)
        
        # 显示互补关系
        complement_sign = MathTex(r"\text{互补}", font_size=28, color=self.COLOR_HIGHLIGHT).next_to(sum_formula, DOWN, buff=0.5)
        self.play(Write(complement_sign), run_time=0.6)
        
        # 显示判定公式
        formula3 = MathTex(r"\text{同旁内角互补}", r"\Rightarrow", r"\text{两直线平行}", font_size=32)
        formula3.move_to(DOWN * 4.5)
        formula3[0].set_color(self.COLOR_HIGHLIGHT)
        formula3[2].set_color(self.COLOR_PRIMARY)
        
        self.play(Write(formula3), run_time=0.8)
        
        # 高亮平行线
        self.play(
            self.parallel_line1.animate.set_color(GREEN),
            self.parallel_line2.animate.set_color(GREEN),
            run_time=0.8
        )
        
        # 总结文字
        summary3 = Text("即：若同旁内角互补，则这两条直线平行", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
        summary3.move_to(DOWN * 5.5)
        
        self.play(Write(summary3), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理：隐藏当前同旁内角相关元素
        self.play(
            FadeOut(co_interior_angle1),
            FadeOut(co_interior_angle2),
            FadeOut(co_int_angle_text1),
            FadeOut(co_int_angle_text2),
            FadeOut(sum_formula),
            FadeOut(complement_sign),
            FadeOut(formula3),
            FadeOut(summary3),
            self.parallel_line1.animate.set_color(self.COLOR_PRIMARY),
            self.parallel_line2.animate.set_color(self.COLOR_PRIMARY),
            run_time=0.8
        )
    
    def show_summary(self):
        """场景5: 三种判定方法总结"""
        # 显示完整的平行线和截线图示
        full_diagram = VGroup(
            self.parallel_line1.copy().set_color(WHITE),
            self.parallel_line2.copy().set_color(WHITE),
            self.transversal.copy().set_color(GRAY_A)
        )
        
        self.play(Create(full_diagram), run_time=0.8)
        
        # 依次显示三种判定方法
        method1 = MathTex(r"\text{1. 同位角相等}", r"\Rightarrow", r"\text{两直线平行}", font_size=28)
        method1[0].set_color(self.COLOR_HIGHLIGHT)
        method1[2].set_color(self.COLOR_PRIMARY)
        method1.move_to(UP * 1.5)
        
        method2 = MathTex(r"\text{2. 内错角相等}", r"\Rightarrow", r"\text{两直线平行}", font_size=28)
        method2[0].set_color(self.COLOR_HIGHLIGHT)
        method2[2].set_color(self.COLOR_PRIMARY)
        method2.move_to(UP * 0.5)
        
        method3 = MathTex(r"\text{3. 同旁内角互补}", r"\Rightarrow", r"\text{两直线平行}", font_size=28)
        method3[0].set_color(self.COLOR_HIGHLIGHT)
        method3[2].set_color(self.COLOR_PRIMARY)
        method3.move_to(UP * (-0.5))
        
        self.play(Write(method1), run_time=0.6)
        self.play(Write(method2), run_time=0.6)
        self.play(Write(method3), run_time=0.6)
        
        # 高亮关键信息
        self.play(
            method1.animate.set_color(YELLOW),
            method2.animate.set_color(YELLOW),
            method3.animate.set_color(YELLOW),
            run_time=0.6
        )
        
        # 强调核心思想
        main_idea = Text("核心思想：由角的关系推断线的关系", font="Noto Sans CJK SC", font_size=28, color=GOLD)
        main_idea.move_to(DOWN * 2)
        
        self.play(Write(main_idea), run_time=0.8)
        
        # 高亮"由角推线"
        angle_to_line = Text("由角的关系推断线的关系", font="Noto Sans CJK SC", font_size=26, color=GOLD)
        angle_to_line.move_to(DOWN * 3)
        
        self.play(Write(angle_to_line), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理部分元素，为结尾做准备
        self.play(
            FadeOut(method1),
            FadeOut(method2), 
            FadeOut(method3),
            FadeOut(main_idea),
            FadeOut(angle_to_line),
            run_time=0.8
        )
    
    def show_outro(self):
        """场景6: 片尾关注"""
        # 完整图示稳定显示
        final_diagram = VGroup(
            self.parallel_line1,
            self.parallel_line2, 
            self.transversal
        )
        
        self.play(final_diagram.animate.set_stroke(width=5), run_time=0.5)
        
        # 作者信息
        author_footer = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_B
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(author_footer, shift=DOWN * 0.2), run_time=0.5)
        
        # 关注提示
        follow_tip = Text("关注我，获得更多数学技巧!", font="Noto Sans CJK SC", font_size=28, color=YELLOW)
        follow_tip.move_to(DOWN * 6.5)
        
        self.play(Write(follow_tip), run_time=0.8)
        
        # 最终强调
        self.play(
            self.parallel_line1.animate.set_stroke(width=6),
            self.parallel_line2.animate.set_stroke(width=6),
            run_time=0.8
        )
        
        self.wait(1.0)
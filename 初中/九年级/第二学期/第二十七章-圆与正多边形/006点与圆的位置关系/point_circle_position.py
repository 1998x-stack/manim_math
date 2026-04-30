"""
点与圆的位置关系 - Point-Circle Position Relationship
使用 Manim 创建的九年级几何教学视频

内容: 点到圆心的距离、点在圆内/圆上/圆外的判断
目标观众: 九年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class PointCirclePosition(Scene):
    """
    点与圆的位置关系教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 距离概念引入
    3. 情况1 - 点在圆内
    4. 情况2 - 点在圆上
    5. 情况3 - 点在圆外
    6. 动态演示
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_CIRCLE = "#3498db"       # 蓝色 - 圆
        self.COLOR_POINT_INSIDE = "#e74c3c" # 红色 - 圆内的点
        self.COLOR_POINT_ON = "#f39c12"     # 橙色 - 圆上的点
        self.COLOR_POINT_OUTSIDE = "#2ecc71"# 绿色 - 圆外的点
        self.COLOR_RADIUS = "#9b59b6"       # 紫色 - 半径
        self.COLOR_DISTANCE = "#e67e22"     # 橙红 - 距离线
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_distance_concept()
        self.show_point_inside()
        self.show_point_on_circle()
        self.show_point_outside()
        self.show_dynamic_demo()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化圆及所有几何元素"""
        # 圆心和半径
        self.O = ORIGIN + UP * 1.5
        self.radius = 1.8
        
        # 三个测试点
        # P1: 圆内 (d < r)
        self.d1 = 1.0  # 距离
        angle1 = 45 * DEGREES
        self.P1 = self.O + self.d1 * np.array([np.cos(angle1), np.sin(angle1), 0])
        
        # P2: 圆上 (d = r)
        angle2 = 120 * DEGREES
        self.P2 = self.O + self.radius * np.array([np.cos(angle2), np.sin(angle2), 0])
        
        # P3: 圆外 (d > r)
        self.d3 = 2.8  # 距离
        angle3 = -30 * DEGREES
        self.P3 = self.O + self.d3 * np.array([np.cos(angle3), np.sin(angle3), 0])
        
        # 验证几何关系
        self.verify_geometry()
        
        print("✓ 几何初始化完成")
    
    def distance_to_center(self, point):
        """计算点到圆心的距离"""
        return np.linalg.norm(point - self.O)
    
    def point_position(self, point):
        """判断点与圆的位置关系"""
        d = self.distance_to_center(point)
        epsilon = 1e-6
        
        if d < self.radius - epsilon:
            return "inside"
        elif abs(d - self.radius) < epsilon:
            return "on"
        else:
            return "outside"
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证P1在圆内
        d1_actual = self.distance_to_center(self.P1)
        if not (d1_actual < self.radius - epsilon):
            print(f"WARNING: P1应该在圆内，但d={d1_actual:.6f}, r={self.radius:.6f}")
        
        # 验证P2在圆上
        d2_actual = self.distance_to_center(self.P2)
        if abs(d2_actual - self.radius) > epsilon:
            print(f"WARNING: P2应该在圆上，但d={d2_actual:.6f}, r={self.radius:.6f}")
        
        # 验证P3在圆外
        d3_actual = self.distance_to_center(self.P3)
        if not (d3_actual > self.radius + epsilon):
            print(f"WARNING: P3应该在圆外，但d={d3_actual:.6f}, r={self.radius:.6f}")
        
        print("✓ 几何验证通过")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "这个点，在圆里还是圆外？",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 圆出现
        self.circle = Circle(
            radius=self.radius,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.O)
        
        self.play(Create(self.circle), run_time=0.8)
        
        # 神秘的点（略模糊位置）
        mystery_point = self.O + self.radius * 0.7 * (RIGHT + UP * 0.5)
        mystery_dot = Dot(mystery_point, color=WHITE, radius=0.10)
        
        self.play(FadeIn(mystery_dot, scale=0.5), run_time=0.6)
        
        # 问号
        question_mark = Text("?", font_size=60, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 2)
        self.play(FadeIn(question_mark, scale=1.2), run_time=0.4)
        self.play(Indicate(question_mark, scale_factor=1.3), run_time=0.5)
        
        self.wait(0.3)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question_mark),
            FadeOut(mystery_dot),
            run_time=0.4
        )
    
    def show_distance_concept(self):
        """场景2: 距离概念引入"""
        # 小标题
        subtitle = Text(
            "关键是距离",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 圆心O出现
        self.dot_O = Dot(self.O, color=self.COLOR_RADIUS, radius=0.12)
        label_O = Text("O", font="PingFang SC", font_size=24, color=self.COLOR_RADIUS).next_to(
            self.dot_O, DOWN, buff=0.15
        )
        
        self.play(
            FadeIn(self.dot_O, scale=0.5),
            FadeIn(label_O),
            run_time=0.5
        )
        
        # 点A在圆上
        angle_A = 60 * DEGREES
        point_A = self.O + self.radius * np.array([np.cos(angle_A), np.sin(angle_A), 0])
        dot_A = Dot(point_A, color=WHITE, radius=0.08)
        label_A = Text("A", font="PingFang SC", font_size=20, color=WHITE).next_to(
            dot_A, UR, buff=0.1
        )
        
        self.play(
            FadeIn(dot_A, scale=0.5),
            FadeIn(label_A),
            run_time=0.6
        )
        
        # 距离线OA
        line_OA = Line(self.O, point_A, color=self.COLOR_RADIUS, stroke_width=3)
        self.play(Create(line_OA), run_time=0.7)
        
        # 标注"r"（半径）
        radius_label = MathTex("r", font_size=28, color=self.COLOR_RADIUS).move_to(
            (self.O + point_A) / 2 + UP * 0.3
        )
        
        self.play(FadeIn(radius_label), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "点到圆心的距离",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation), run_time=0.7)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(dot_A),
            FadeOut(label_A),
            FadeOut(line_OA),
            FadeOut(radius_label),
            FadeOut(explanation),
            FadeOut(label_O),
            run_time=0.5
        )
    
    def show_point_inside(self):
        """场景3: 情况1 - 点在圆内"""
        # 小标题
        subtitle = Text(
            "情况1：点在圆内",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_POINT_INSIDE
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 点P1出现
        dot_P1 = Dot(self.P1, color=self.COLOR_POINT_INSIDE, radius=0.12)
        label_P1 = Text("P", font="PingFang SC", font_size=22, color=WHITE).next_to(
            dot_P1, RIGHT, buff=0.15
        )
        
        self.play(
            FadeIn(dot_P1, scale=0.5),
            FadeIn(label_P1),
            run_time=0.6
        )
        
        # 距离线OP1
        line_OP1 = Line(self.O, self.P1, color=self.COLOR_POINT_INSIDE, stroke_width=3)
        self.play(Create(line_OP1), run_time=0.7)
        
        # 距离标注"d"
        d1_value = self.distance_to_center(self.P1)
        distance_label = MathTex("d", font_size=26, color=self.COLOR_POINT_INSIDE).move_to(
            (self.O + self.P1) / 2 + LEFT * 0.3
        )
        
        self.play(FadeIn(distance_label), run_time=0.5)
        
        # 半径参考线（虚线到圆上）
        radius_point = self.O + self.radius * (self.P1 - self.O) / np.linalg.norm(self.P1 - self.O)
        radius_reference = DashedLine(
            self.P1, radius_point,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08,
            stroke_width=2
        )
        
        self.play(Create(radius_reference), run_time=0.8)
        
        # 半径标注"r"
        radius_label = MathTex("r", font_size=26, color=self.COLOR_RADIUS).move_to(
            (self.O + radius_point) / 2 + RIGHT * 0.3
        )
        
        self.play(FadeIn(radius_label), run_time=0.5)
        
        # 不等式
        formula = MathTex(
            r"d < r",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(formula, shift=UP * 0.3), run_time=0.8)
        
        # 说明
        explanation = Text(
            "距离小于半径 → 点在圆内",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(dot_P1),
            FadeOut(label_P1),
            FadeOut(line_OP1),
            FadeOut(distance_label),
            FadeOut(radius_reference),
            FadeOut(radius_label),
            FadeOut(formula),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_point_on_circle(self):
        """场景4: 情况2 - 点在圆上"""
        # 小标题
        subtitle = Text(
            "情况2：点在圆上",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_POINT_ON
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 点P2出现
        dot_P2 = Dot(self.P2, color=self.COLOR_POINT_ON, radius=0.12)
        label_P2 = Text("P", font="PingFang SC", font_size=22, color=WHITE).next_to(
            dot_P2, LEFT, buff=0.15
        )
        
        self.play(
            FadeIn(dot_P2, scale=0.5),
            FadeIn(label_P2),
            run_time=0.6
        )
        
        # 距离线OP2（也是半径）
        line_OP2 = Line(self.O, self.P2, color=self.COLOR_POINT_ON, stroke_width=3)
        self.play(Create(line_OP2), run_time=0.7)
        
        # 距离和半径标注（重叠，表示相等）
        dr_label = MathTex("d = r", font_size=28, color=self.COLOR_POINT_ON).move_to(
            (self.O + self.P2) / 2 + LEFT * 0.4
        )
        
        self.play(FadeIn(dr_label), run_time=0.7)
        
        # 等式
        formula = MathTex(
            r"d = r",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(formula, shift=UP * 0.3), run_time=0.8)
        
        # 说明
        explanation = Text(
            "距离等于半径 → 点在圆上",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.6)
        
        # 圆周闪烁
        self.play(Indicate(self.circle, color=self.COLOR_POINT_ON), run_time=1.0)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(dot_P2),
            FadeOut(label_P2),
            FadeOut(line_OP2),
            FadeOut(dr_label),
            FadeOut(formula),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_point_outside(self):
        """场景5: 情况3 - 点在圆外"""
        # 小标题
        subtitle = Text(
            "情况3：点在圆外",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_POINT_OUTSIDE
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 点P3出现
        dot_P3 = Dot(self.P3, color=self.COLOR_POINT_OUTSIDE, radius=0.12)
        label_P3 = Text("P", font="PingFang SC", font_size=22, color=WHITE).next_to(
            dot_P3, RIGHT, buff=0.15
        )
        
        self.play(
            FadeIn(dot_P3, scale=0.5),
            FadeIn(label_P3),
            run_time=0.6
        )
        
        # 距离线OP3
        line_OP3 = Line(self.O, self.P3, color=self.COLOR_POINT_OUTSIDE, stroke_width=3)
        self.play(Create(line_OP3), run_time=0.7)
        
        # 距离标注"d"
        distance_label = MathTex("d", font_size=26, color=self.COLOR_POINT_OUTSIDE).move_to(
            (self.O + self.P3) / 2 + DOWN * 0.3
        )
        
        self.play(FadeIn(distance_label), run_time=0.5)
        
        # 半径参考线（虚线到圆上）
        radius_point = self.O + self.radius * (self.P3 - self.O) / np.linalg.norm(self.P3 - self.O)
        radius_reference = DashedLine(
            self.O, radius_point,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08,
            stroke_width=2
        )
        
        self.play(Create(radius_reference), run_time=0.8)
        
        # 半径标注"r"
        radius_label = MathTex("r", font_size=26, color=self.COLOR_RADIUS).move_to(
            (self.O + radius_point) / 2 + UP * 0.3
        )
        
        self.play(FadeIn(radius_label), run_time=0.5)
        
        # 不等式
        formula = MathTex(
            r"d > r",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(formula, shift=UP * 0.3), run_time=0.8)
        
        # 对比：d 更长
        self.play(
            Indicate(line_OP3, color=self.COLOR_HIGHLIGHT),
            Indicate(radius_reference, color=self.COLOR_HIGHLIGHT),
            run_time=1.0
        )
        
        # 说明
        explanation = Text(
            "距离大于半径 → 点在圆外",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(dot_P3),
            FadeOut(label_P3),
            FadeOut(line_OP3),
            FadeOut(distance_label),
            FadeOut(radius_reference),
            FadeOut(radius_label),
            FadeOut(formula),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_dynamic_demo(self):
        """场景6: 动态演示"""
        # 小标题
        subtitle = Text(
            "动态演示",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 初始点（圆外）
        start_pos = self.O + 2.5 * RIGHT
        dot_P = Dot(start_pos, color=self.COLOR_POINT_OUTSIDE, radius=0.12)
        
        self.play(FadeIn(dot_P, scale=0.5), run_time=0.6)
        
        # 距离线（动态更新）
        line_OP = always_redraw(
            lambda: Line(self.O, dot_P.get_center(), color=dot_P.get_color(), stroke_width=3)
        )
        
        self.add(line_OP)
        
        # 距离值（动态更新）
        distance_value = always_redraw(
            lambda: MathTex(
                f"d = {np.linalg.norm(dot_P.get_center() - self.O):.2f}",
                font_size=24,
                color=WHITE
            ).move_to(DOWN * 4)
        )
        
        self.add(distance_value)
        
        # 半径标注（固定）
        radius_text = MathTex(
            f"r = {self.radius:.2f}",
            font_size=24,
            color=self.COLOR_RADIUS
        ).move_to(DOWN * 4.8)
        
        self.play(FadeIn(radius_text), run_time=0.4)
        
        # 状态文字（动态更新）
        def get_status_text():
            d = np.linalg.norm(dot_P.get_center() - self.O)
            if d < self.radius - 0.05:
                return Text("圆内", font="PingFang SC", font_size=28, color=self.COLOR_POINT_INSIDE)
            elif abs(d - self.radius) < 0.05:
                return Text("圆上", font="PingFang SC", font_size=28, color=self.COLOR_POINT_ON)
            else:
                return Text("圆外", font="PingFang SC", font_size=28, color=self.COLOR_POINT_OUTSIDE)
        
        status_text = always_redraw(lambda: get_status_text().move_to(DOWN * 5.8))
        
        self.add(status_text)
        
        self.wait(1.0)
        
        # P移动到圆上
        on_circle_pos = self.O + self.radius * RIGHT
        self.play(
            dot_P.animate.move_to(on_circle_pos).set_color(self.COLOR_POINT_ON),
            run_time=1.5
        )
        
        self.wait(1.5)
        
        # P移动到圆内
        inside_pos = self.O + 1.2 * RIGHT
        self.play(
            dot_P.animate.move_to(inside_pos).set_color(self.COLOR_POINT_INSIDE),
            run_time=1.5
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(dot_P),
            FadeOut(line_OP),
            FadeOut(distance_value),
            FadeOut(radius_text),
            FadeOut(status_text),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 总结与片尾"""
        # 圆和圆心缩小上移
        self.play(
            VGroup(self.circle, self.dot_O).animate.scale(0.5).move_to(UP * 4.5),
            run_time=1.0
        )
        
        # 知识卡片
        cards = VGroup()
        
        # 卡片1
        card_1 = self.create_knowledge_card(
            "d < r → 圆内",
            "距离小于半径",
            self.COLOR_POINT_INSIDE,
            UP * 2
        )
        cards.add(card_1)
        
        # 卡片2
        card_2 = self.create_knowledge_card(
            "d = r → 圆上",
            "距离等于半径",
            self.COLOR_POINT_ON,
            UP * 0.5
        )
        cards.add(card_2)
        
        # 卡片3
        card_3 = self.create_knowledge_card(
            "d > r → 圆外",
            "距离大于半径",
            self.COLOR_POINT_OUTSIDE,
            DOWN * 1
        )
        cards.add(card_3)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 0), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.3)
        
        self.wait(1.0)
        
        # 总结文字
        summary_text = Text(
            "掌握距离判断\n轻松解决位置关系！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(summary_text, shift=UP * 0.3, scale=1.05), run_time=0.6)
        
        self.wait(1.0)
        
        # 清理并准备片尾
        self.play(
            FadeOut(VGroup(self.circle, self.dot_O)),
            FadeOut(cards),
            FadeOut(summary_text),
            run_time=0.6
        )
        
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
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多几何技巧！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 小圆形装饰
        circles = VGroup(*[
            Circle(radius=0.15, color=self.COLOR_CIRCLE, fill_opacity=0.8)
            .move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(circ, scale=0.5) for circ in circles],
            run_time=0.6
        )
        self.play(Rotate(circles, angle=PI, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(circles),
            run_time=1.0
        )
    
    def create_knowledge_card(self, title, content, color, position):
        """创建知识卡片"""
        # 图标圆
        icon = Circle(radius=0.15, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        
        # 内容
        content_text = Text(
            content,
            font="PingFang SC",
            font_size=16,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.25)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card


# 运行命令:
# manim -pql point_circle_position.py PointCirclePosition  # 快速预览
# manim -qh point_circle_position.py PointCirclePosition   # 高质量渲染
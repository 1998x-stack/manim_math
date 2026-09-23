"""y=A sin(ωx+φ)+B 教学动画的独立数学检查。

可单独运行：python verify_geometry.py。无需 Manim；不验证最终画面或 TeX 编译。
"""

from math import isclose, pi, sin


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sine_properties(a, omega, phi, b):
    """返回可观察的值域、最小正周期和水平位移；常函数周期记为 None。"""
    if omega == 0:
        value = a * sin(phi) + b
        return {'range': (value, value), 'period': None, 'horizontal_shift': None}
    if a == 0:
        return {'range': (b, b), 'period': None, 'horizontal_shift': None}
    return {'range': (b - abs(a), b + abs(a)),
            'period': 2 * pi / abs(omega),
            'horizontal_shift': -phi / omega}


def verify_angles():
    require(isclose(pi / 4 * 180 / pi, 45), 'π/4 的角度转换错误')
    require(isclose(3 * pi / 2 * 180 / pi, 270), '3π/2 的角度转换错误')
    print('PASS: 弧度与角度换算；不替代 Manim Angle 方向检查')


def verify_trigonometric_transform():
    examples = ((1, 1, 0, 0), (2, 2, pi / 4, 1),
                (-3, -2, -pi / 2, -1), (0, 1, 0, 2),
                (2, 0, pi / 2, 1))
    for a, omega, phi, b in examples:
        properties = sine_properties(a, omega, phi, b)
        lo, hi = properties['range']
        if not omega or not a:
            require(properties['period'] is None, '常函数不能标注有限最小正周期')
            require(properties['horizontal_shift'] is None, '常函数不具有可观察的水平位移')
            for x in (-pi, -1, 0, 1, pi):
                require(isclose(a * sin(omega * x + phi) + b, lo, abs_tol=1e-10),
                        '常函数值域错误')
            continue
        x_max_phase = (pi / 2 - phi) / omega
        x_min_phase = (3 * pi / 2 - phi) / omega
        actual = sorted((a * sin(omega * x_max_phase + phi) + b,
                         a * sin(omega * x_min_phase + phi) + b))
        require(isclose(actual[0], lo, abs_tol=1e-10) and
                isclose(actual[1], hi, abs_tol=1e-10), '振幅/纵向平移和值域不一致')
        require(isclose(a * sin(omega * properties['horizontal_shift'] + phi) + b,
                        b, abs_tol=1e-10), '水平位移公式应为 -φ/ω')
        for x in (-pi, -1, 0, 1, pi):
            y = a * sin(omega * x + phi) + b
            shifted_y = a * sin(omega * (x + properties['period']) + phi) + b
            require(isclose(y, shifted_y, rel_tol=1e-10, abs_tol=1e-10),
                    '周期公式应为 2π/|ω|')
    print('PASS: 振幅、周期、相位、值域及 A=0/ω=0 退化情形')


def grep_MathTex():
    """历史函数名保留供其他脚本调用，不伪称编译已验证。"""
    print('SKIP: LaTeX 表达式须通过实际 Manim/TeX 渲染验证')


def verify_boundaries():
    """仅检查源场景所定义坐标轴的理论宽高，文本须另外目视检查。"""
    frame_width, frame_height = 9, 16
    axes_width, axes_height = 8 * 0.65, 10 * 0.65
    axes_center_y = -0.5
    require(axes_width < frame_width, '坐标轴宽度溢出画面')
    require(abs(axes_center_y) + axes_height / 2 < frame_height / 2,
            '坐标轴高度溢出画面')
    print('PASS: 基础坐标轴理论边界；标题、字幕、动效仍需渲染检查')


def main():
    verify_angles()
    verify_trigonometric_transform()
    verify_boundaries()
    grep_MathTex()
    print('PASS: 已执行的纯 Python 数学与几何检查')


if __name__ == '__main__':
    main()

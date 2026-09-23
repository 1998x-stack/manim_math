"""Guarded, one-shot high-school scene repair. Do not run on unrelated code.

Only three reviewed high-one lesson sources are eligible; all edits are checked
against expected patterns and AST before a write. The GitHub workflow that uses
this script must run only on the isolated repair branch, never a PR head.
"""
import argparse
import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANGLE = ROOT / '高中/高一/第二学期/第五章-三角比/001任意角与弧度制/001_任意角与弧度制.py'
RATIO = ROOT / '高中/高一/第二学期/第五章-三角比/002任意角的三角比/any_angle_trigonometry.py'
SINE = ROOT / '高中/高一/第二学期/第六章-三角函数/003函数y=Asin(ωx+φ)的图像与性质/003_函数y=Asin(ωx+φ)的图像与性质.py'


def once(text, old, new):
    count = text.count(old)
    if count != 1:
        raise AssertionError(f'Expected exactly one {old!r}, found {count}')
    return text.replace(old, new, 1)


def patch_degrees(text, variable):
    if variable == 'angle':
        old = 'f"{self.ANGLE_DEG}°"'
        new = r'rf"{self.ANGLE_DEG}^{{\circ}}"'
    else:
        old = 'f"{int(angle*180/PI)}°"'
        new = r'rf"{int(round(np.degrees(angle)))}^{{\circ}}"'
    return once(text, old, new)


def _span(source, node):
    # CPython AST columns are UTF-8 *byte* offsets, not Unicode string indices.
    lines = source.splitlines(keepends=True)
    start = (sum(map(len, lines[:node.lineno - 1]))
             + len(lines[node.lineno - 1].encode('utf-8')[:node.col_offset].decode('utf-8')))
    end = (sum(map(len, lines[:node.end_lineno - 1]))
           + len(lines[node.end_lineno - 1].encode('utf-8')[:node.end_col_offset].decode('utf-8')))
    return start, end


def _tex_with_chinese(node):
    return (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
            and node.func.id == 'Tex' and len(node.args) == 1
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
            and any('\u4e00' <= c <= '\u9fff' for c in node.args[0].value))


def _play(call):
    return (isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute)
            and call.func.attr == 'play' and isinstance(call.func.value, ast.Name)
            and call.func.value.id == 'self')


def _convert_tex(node, source):
    content = node.args[0].value
    kw = {k.arg: ast.get_source_segment(source, k.value) for k in node.keywords if k.arg}
    if set(kw) - {'font_size', 'color'}:
        raise AssertionError(f'Unexpected Tex kwargs: {kw}')
    size, color = kw.get('font_size', '24'), kw.get('color', 'WHITE')

    def text(s):
        return f'Text({s!r}, font="PingFang SC", font_size={size}, color={color})'

    def math(s):
        return f'MathTex(r"{s}", font_size={size}, color={color})'

    def together(*parts):
        return 'VGroup(' + ', '.join(parts) + ').arrange(RIGHT, buff=0.12)'

    # Keep fractions and mathematical variables in MathTex while CJK uses Text.
    if content == r'周期 T = \frac{2\pi}{\omega}':
        return together(text('周期：'), math(r'T=\frac{2\pi}{|\omega|}'))
    if content == r'左移 $\frac{\pi}{8}$':
        return together(text('左移'), math(r'\frac{\pi}{8}'))
    if content == r'相位: $\omega x + \varphi$, 初相: $\varphi$':
        return together(text('相位：'), math(r'\omega x+\varphi'), text('初相：'), math(r'\varphi'))
    if content == r'• $\omega$: 频率，控制周期 $T = \frac{2\pi}{\omega}$':
        return together(text('• ω：频率，周期'), math(r'T=\frac{2\pi}{|\omega|}'))

    replacements = ((r'\omega', 'ω'), (r'\varphi', 'φ'), (r'\pi', 'π'))
    cleaned = content.replace('$', '')
    for old, new in replacements:
        cleaned = cleaned.replace(old, new)
    if '\\' in cleaned:
        raise AssertionError(f'Unconverted TeX command in Chinese label: {content!r}')
    if cleaned == 'A越大，图像拉伸越厉害':
        cleaned = '|A| 越大，振幅越大（A<0 时图像翻折）'
    return text(cleaned)


def patch_sine(source):
    tree = ast.parse(source)
    edits = []
    converted = 0
    nested = 0
    for node in ast.walk(tree):
        if _tex_with_chinese(node):
            edits.append((*_span(source, node), _convert_tex(node, source)))
            converted += 1
        if _play(node) and any(_play(arg) for arg in node.args):
            original = ast.get_source_segment(source, node)
            if 'run_time=0.8' in original:
                replacement = 'self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=0.8)'
            elif 'run_time=1.0' in original:
                replacement = 'self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=1.0)'
            else:
                raise AssertionError('Unexpected nested self.play timing')
            edits.append((*_span(source, node), replacement))
            nested += 1
    if (converted, nested) != (19, 2):
        raise AssertionError(f'Expected 19 Tex labels and 2 nested self.play, got {converted}, {nested}')
    for start, end, replacement in sorted(edits, reverse=True):
        source = source[:start] + replacement + source[end:]
    source = once(source, 'self.x_range = [-4, 4, 1]  # x范围',
                  'self.x_range = [-2*np.pi, 2*np.pi, np.pi/2]  # 覆盖整段 2π 周期')
    ast.parse(source)
    return source


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Actually write changed sources')
    args = parser.parse_args(argv)
    for path, patch in ((ANGLE, lambda src: patch_degrees(src, 'angle')),
                        (RATIO, lambda src: patch_degrees(src, 'ratio')),
                        (SINE, patch_sine)):
        before = path.read_text(encoding='utf-8')
        after = patch(before)
        assert after != before, path
        ast.parse(after, filename=str(path))
        if args.apply:
            path.write_text(after, encoding='utf-8')
        print(('applied: ' if args.apply else 'checked: ') + str(path.relative_to(ROOT)))


if __name__ == '__main__':
    main()

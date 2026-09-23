#!/usr/bin/env python3
"""Read-only static audit of 高中/高一 Python sources (no Manim installation needed).

Exit status 1 means a Python source failed to parse; warnings are review candidates,
not verified scene defects. This does not validate math, fonts or rendered frames.
"""

import argparse
import ast
import json
from collections import Counter
from pathlib import Path
import re

DEFAULT_ROOT = Path(__file__).resolve().parents[1] / '高中' / '高一'
CJK = re.compile(r'[\u3400-\u9fff]')
SCENE_BASES = {'Scene', 'MovingCameraScene', 'ThreeDScene', 'ZoomedScene',
               'LinearTransformationScene'}
ANIMATIONS = {'Write', 'Create', 'FadeIn', 'FadeOut', 'Indicate',
              'Transform', 'ReplacementTransform', 'GrowFromCenter',
              'DrawBorderThenFill', 'Uncreate', 'Unwrite'}


def call_name(func):
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return ''


def scene_names(tree):
    return [node.name for node in tree.body if isinstance(node, ast.ClassDef)
            and any(call_name(base) in SCENE_BASES for base in node.bases)]


def duplicate_play_targets(tree):
    """Only detect repeated simple targets in the same *direct* self.play call."""
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
            continue
        if node.func.attr != 'play' or not isinstance(node.func.value, ast.Name) or node.func.value.id != 'self':
            continue
        seen = {}
        for arg in node.args:
            if not isinstance(arg, ast.Call) or call_name(arg.func) not in ANIMATIONS or not arg.args:
                continue
            target = arg.args[0]
            if isinstance(target, ast.Name):
                key = target.id
            elif (isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name)
                  and target.value.id == 'self'):
                key = 'self.' + target.attr
            else:
                continue
            if key in seen:
                yield node.lineno, key
            else:
                seen[key] = arg.lineno


def audit_source(source, filename='<input>'):
    findings = []
    try:
        tree = ast.parse(source, filename=filename)
        compile(tree, filename, 'exec')
    except (SyntaxError, ValueError) as error:
        findings.append({'line': getattr(error, 'lineno', None), 'severity': 'error',
                         'rule': 'python-syntax', 'message': str(error)})
        return [], findings
    names = scene_names(tree)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and call_name(node.func) in {'MathTex', 'Tex'}:
            args = [*node.args, *(kw.value for kw in node.keywords)]
            if any(isinstance(value, ast.Constant) and isinstance(value.value, str)
                   and CJK.search(value.value) for value in args):
                findings.append({'line': node.lineno, 'severity': 'warning',
                                 'rule': 'chinese-in-tex',
                                 'message': '公式字符串包含中文，请验证 XeLaTeX 环境或改用 Text'})
        if isinstance(node, ast.Assign) and any(
                isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name)
                and target.value.id == 'config' and target.attr in
                {'frame_width', 'frame_height', 'pixel_width', 'pixel_height'}
                for target in node.targets):
            if node in tree.body:
                findings.append({'line': node.lineno, 'severity': 'info',
                                 'rule': 'module-config',
                                 'message': '导入模块时修改全局 Manim 配置；多场景复用请检查隔离'})
    for line, target in duplicate_play_targets(tree):
        findings.append({'line': line, 'severity': 'warning',
                         'rule': 'duplicate-play-target',
                         'message': f'同一个 self.play 中多次动画化 {target}；检查并行动画冲突'})
    return names, sorted(findings, key=lambda item: (item['line'] or 0, item['rule']))


def audit(root):
    if not root.is_dir():
        raise FileNotFoundError(f'高一目录不存在：{root}')
    files = []
    findings = []
    paths = sorted(root.rglob('*.py'))
    if not paths:
        raise FileNotFoundError(f'高一目录没有 Python 文件：{root}')
    for path in paths:
        relative = path.relative_to(root).as_posix()
        try:
            source = path.read_text(encoding='utf-8')
        except (UnicodeError, OSError) as error:
            names, local = [], [{'line': None, 'severity': 'error',
                                  'rule': 'read-failure', 'message': str(error)}]
        else:
            names, local = audit_source(source, str(path))
        files.append({'path': relative, 'semester': relative.split('/', 1)[0],
                      'scenes': names, 'syntax': not any(f['severity'] == 'error' for f in local)})
        findings.extend({'path': relative, **finding} for finding in local)
    return {'root': str(root), 'python_count': len(files),
            'scene_count': sum(len(item['scenes']) for item in files),
            'by_semester': dict(sorted(Counter(item['semester'] for item in files).items())),
            'files': files, 'findings': findings}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=DEFAULT_ROOT)
    parser.add_argument('--json', action='store_true', help='输出完整机器可读检查记录')
    args = parser.parse_args(argv)
    try:
        result = audit(args.root)
    except (FileNotFoundError, OSError) as error:
        parser.exit(2, f'{error}\n')
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"高一源码：{result['python_count']} 个；直接识别 Scene：{result['scene_count']} 个")
        print(f"学期统计：{result['by_semester']}")
        for finding in result['findings']:
            print(f"{finding['severity']}: {finding['path']}:{finding['line'] or '-'} "
                  f"[{finding['rule']}] {finding['message']}")
        print('静态检查不等于数学验证、Manim 渲染或画面验收。')
    return int(any(finding['severity'] == 'error' for finding in result['findings']))


if __name__ == '__main__':
    raise SystemExit(main())

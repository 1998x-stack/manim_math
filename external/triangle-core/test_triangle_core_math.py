"""Mathematical regression for five scenes, without importing Manim.

Run from repository root: python -m unittest discover -s external/triangle-core \
    -p test_triangle_core_math.py -v
"""
import ast
import math
from pathlib import Path
import re
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SCENES = {
    "angles": ("初中/七年级/第二学期/第十四章-三角形/003三角形的内角和定理/triangle_angle_visual.py", "TriangleAngleSumVisual"),
    "sides": ("初中/七年级/第二学期/第十四章-三角形/002三角形的三边关系/triangle_inequality_visual.py", "TriangleInequalityVisual"),
    "similarity": ("初中/七年级/第二学期/第十四章-三角形/005全等三角形的概念与性质/congruence_similarity_visual.py", "CongruenceSimilarityVisual"),
    "centers": ("external/triangle-core/four-centers/four_centers_visual.py", "FourCentersVisual"),
    "laws": ("高中/高一/第二学期/第五章-三角比/008解斜三角形/triangle_laws_visual.py", "TriangleLawsVisual"),
}


def pure_function(scene_key, name):
    """Compile precisely the repository function's AST, without Manim imports."""
    path = ROOT / SCENES[scene_key][0]
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    selected = [node for node in tree.body
                if isinstance(node, ast.FunctionDef) and node.name == name]
    if len(selected) != 1:
        raise AssertionError(f"Missing unique pure function {name}: {path}")
    isolated = ast.fix_missing_locations(ast.Module(body=selected, type_ignores=[]))
    namespace = {"np": np, "math": math}
    exec(compile(isolated, str(path), "exec"), namespace)
    return namespace[name]


def angle(p, q, r):
    u, v = p - q, r - q
    cosine = np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)
    return math.acos(float(np.clip(cosine, -1, 1)))


class TriangleCoreMathTests(unittest.TestCase):
    def test_all_scene_sources_compile_and_use_correct_apis(self):
        for key, (relative, class_name) in SCENES.items():
            with self.subTest(scene=key):
                path = ROOT / relative
                source = path.read_text(encoding="utf-8")
                compile(source, str(path), "exec")
                tree = ast.parse(source)
                self.assertTrue(any(isinstance(n, ast.ClassDef) and n.name == class_name
                                    and any(isinstance(base, ast.Name) and base.id == "Scene"
                                            for base in n.bases) for n in tree.body))
                for node in ast.walk(tree):
                    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                            and node.func.id in {"MathTex", "Tex"}:
                        for arg in node.args:
                            if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                                self.assertIsNone(re.search(r"[\u3400-\u9fff]", arg.value))
                    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                            and node.func.attr == "play":
                        self.assertFalse(any(isinstance(arg, ast.Call)
                                             and isinstance(arg.func, ast.Attribute)
                                             and arg.func.attr == "play" for arg in node.args))

    def test_angle_sum_and_exterior(self):
        a = np.array([-2.7, -1.1]); b = np.array([2.7, -1.1])
        for x in (-1.3, -0.6, 0.2, 1.2):
            c = np.array([x, 2.1 + 0.18 * x])
            alpha, beta, gamma = angle(b, a, c), angle(a, b, c), angle(a, c, b)
            self.assertAlmostEqual(alpha + beta + gamma, math.pi, places=10)
            self.assertAlmostEqual(math.pi - beta, alpha + gamma, places=10)

    def test_strict_triangle_inequality_and_construction(self):
        construct = pure_function("sides", "upper_vertex")
        a = np.array([-1.6, -1.1, 0.0]); b = np.array([1.6, -1.1, 0.0])
        for ac in (1.01, 1.8, 2.2, 3.6, 5.39):
            c = construct(3.2, ac, 2.2)
            self.assertIsNotNone(c)
            self.assertGreater(c[1], a[1])
            self.assertAlmostEqual(np.linalg.norm(c - a), ac, places=8)
            self.assertAlmostEqual(np.linalg.norm(c - b), 2.2, places=8)
        for ac in (-1, 0, 0.8, 1.0, 5.4, 5.6):
            self.assertIsNone(construct(3.2, ac, 2.2))

    def test_congruence_similarity_distinction(self):
        p = np.array([[-1.1, -0.8], [1.1, -0.8], [-0.35, 1.2]])
        theta = math.pi / 3
        rot = np.array([[math.cos(theta), -math.sin(theta)],
                        [math.sin(theta), math.cos(theta)]])
        q = p @ rot.T + np.array([1.65, 0])
        scaled = (q - [1.65, 0]) * 1.35 + [1.65, 0]
        for j, k in ((0, 1), (1, 2), (2, 0)):
            original = np.linalg.norm(p[j] - p[k])
            self.assertAlmostEqual(original, np.linalg.norm(q[j] - q[k]))
            self.assertAlmostEqual(1.35 * original,
                                   np.linalg.norm(scaled[j] - scaled[k]))
            self.assertNotAlmostEqual(original, np.linalg.norm(scaled[j] - scaled[k]))
        for j, k, m in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
            self.assertAlmostEqual(angle(p[k], p[j], p[m]),
                                   angle(scaled[k], scaled[j], scaled[m]))

    def test_four_centers_and_euler_line(self):
        centers = pure_function("centers", "triangle_centers")
        a = np.array([-2.2, -0.5, 0]); b = np.array([2.2, -0.5, 0])
        for c in (np.array([-0.7, 2.0, 0]), np.array([1.4, 0.3, 0]),
                  np.array([0.0, 2.0, 0])):
            g, o, h, i = centers(a, b, c)
            self.assertTrue(np.allclose(g, (a + b + c) / 3))
            self.assertTrue(np.allclose(h, 3 * g - 2 * o))
            for vertex in (b, c):
                self.assertAlmostEqual(np.linalg.norm(o - a),
                                       np.linalg.norm(o - vertex), places=8)
            self.assertAlmostEqual(np.dot(h - a, b - c), 0.0, places=8)
            self.assertAlmostEqual(np.dot(h - b, a - c), 0.0, places=8)
            distances = []
            for u, v in ((a, b), (b, c), (c, a)):
                edge = v[:2] - u[:2]
                distances.append(abs(np.linalg.det(np.array([edge, i[:2] - u[:2]])))
                                 / np.linalg.norm(edge))
            self.assertTrue(np.allclose(distances, distances[0], atol=1e-8))
            self.assertTrue(np.allclose(g - o, (h - o) / 3))
        with self.assertRaises(ValueError):
            centers(a, b, np.array([0.0, -0.5, 0]))

    def test_sine_cosine_laws_obtuse_and_acute(self):
        a = np.array([-2.0, -0.8]); b = np.array([2.0, -0.8])
        for c in (np.array([-0.5, 1.9]), np.array([0.7, 1.65]),
                  np.array([2.7, 0.8])):
            side_a, side_b, side_c = (np.linalg.norm(b - c),
                                      np.linalg.norm(a - c), np.linalg.norm(a - b))
            alpha, beta, gamma = angle(b, a, c), angle(a, b, c), angle(a, c, b)
            area2 = abs(float(np.linalg.det(np.array([b - a, c - a]))))
            for product in (side_b * side_c * math.sin(alpha),
                            side_c * side_a * math.sin(beta),
                            side_a * side_b * math.sin(gamma)):
                self.assertAlmostEqual(product, area2, places=8)
            radius = side_a * side_b * side_c / (2 * area2)
            for side, theta in ((side_a, alpha), (side_b, beta),
                                (side_c, gamma)):
                self.assertAlmostEqual(side / math.sin(theta), 2 * radius, places=8)
            self.assertAlmostEqual(side_a ** 2, side_b ** 2 + side_c ** 2
                                   - 2 * side_b * side_c * math.cos(alpha), places=8)


if __name__ == "__main__":
    unittest.main()

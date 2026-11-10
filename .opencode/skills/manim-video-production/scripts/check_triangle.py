#!/usr/bin/env python3
"""Check a triangle and its circumcenter numerically using only Python stdlib."""
import argparse
import json
import math
import sys


def check(points):
    if len(points) != 3 or any(len(p) != 2 or any(not math.isfinite(v) for v in p) for p in points):
        raise ValueError("three finite 2D points required")
    (ax, ay), (bx, by), (cx, cy) = points
    u = (bx - ax, by - ay)
    v = (cx - ax, cy - ay)
    scale = max(math.hypot(*u), math.hypot(*v), math.hypot(bx-cx, by-cy))
    if scale == 0:
        raise ValueError("degenerate triangle: all points coincide")
    determinant = 2 * (u[0] * v[1] - u[1] * v[0])
    if abs(determinant) <= 2e-12 * scale * scale:
        raise ValueError("degenerate or nearly collinear triangle; no reliable circumcenter")
    uu = u[0] ** 2 + u[1] ** 2
    vv = v[0] ** 2 + v[1] ** 2
    ox = ax + (uu * v[1] - vv * u[1]) / determinant
    oy = ay + (vv * u[0] - uu * v[0]) / determinant
    radii = [math.hypot(px - ox, py - oy) for px, py in points]
    residual = max(radii) - min(radii)
    tolerance = 1e-9 * max(scale, *radii)
    if not all(math.isfinite(x) for x in (ox, oy, residual)) or residual > tolerance:
        raise ValueError("numeric stability check failed")
    return {"status": "numeric_check_only", "circumcenter": [ox, oy], "radius": radii[0], "residual": residual, "tolerance": tolerance}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--points", required=True, help="ax,ay;bx,by;cx,cy")
    args = parser.parse_args(argv)
    try:
        pts = [list(map(float, pair.split(","))) for pair in args.points.split(";")]
        result = check(pts)
    except (ValueError, OverflowError, ZeroDivisionError) as exc:
        print(f"check_triangle: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

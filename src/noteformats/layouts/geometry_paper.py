from __future__ import annotations

from math import cos, pi, sin, sqrt

from ..geometry import Scene


def _clipped(s: Scene, x0, y0, dx, dy, layer="light"):
    bounds = (s.left, s.top, s.right, s.bottom)
    left, top, right, bottom = bounds
    hits = []
    if abs(dx) > 1e-9:
        for x in (left, right):
            t = (x - x0) / dx
            y = y0 + t * dy
            if top - 1e-7 <= y <= bottom + 1e-7:
                hits.append((t, x, max(top, min(bottom, y))))
    if abs(dy) > 1e-9:
        for y in (top, bottom):
            t = (y - y0) / dy
            x = x0 + t * dx
            if left - 1e-7 <= x <= right + 1e-7:
                hits.append((t, max(left, min(right, x)), y))
    if len(hits) >= 2:
        hits.sort()
        s.line(hits[0][1], hits[0][2], hits[-1][1], hits[-1][2], layer)


def triangular_grid(s: Scene, p: dict):
    side = 10
    rise = side * sqrt(3) / 2
    y = s.top
    while y <= s.bottom:
        s.line(s.left, y, s.right, y, "light")
        y += rise
    spread = s.height / sqrt(3)
    x = s.left - spread - side
    while x <= s.right + spread + side:
        _clipped(s, x, s.top, 1, sqrt(3))
        _clipped(s, x, s.bottom, 1, -sqrt(3))
        x += side
    for x, y in ((s.left + 8, s.top + 16), (s.left + 45, s.top + 67), (s.left + 20, s.top + 117)):
        s.slot(x, y, 30)


def hex_grid(s: Scene, p: dict):
    radius = 6.2
    x_step, y_step = sqrt(3) * radius, 1.5 * radius
    edges = set()
    row = 0
    y = s.top + radius
    while y + radius <= s.bottom:
        x = s.left + sqrt(3) * radius / 2 + (x_step / 2 if row % 2 else 0)
        while x + sqrt(3) * radius / 2 <= s.right:
            pts = [(x + radius * cos(-pi / 2 + i * pi / 3), y + radius * sin(-pi / 2 + i * pi / 3)) for i in range(6)]
            if all(s.left <= px <= s.right and s.top <= py <= s.bottom for px, py in pts):
                for a, b in zip(pts, pts[1:] + pts[:1]):
                    key = tuple(sorted(((round(a[0], 3), round(a[1], 3)), (round(b[0], 3), round(b[1], 3)))))
                    edges.add(key)
            x += x_step
        y += y_step
        row += 1
    for a, b in sorted(edges):
        s.line(*a, *b, "light")
    for x, y in ((s.left + 5, s.top + 15), (s.left + 44, s.top + 70), (s.left + 5, s.top + 124)):
        s.slot(x, y, 32)


def rhombus_grid(s: Scene, p: dict):
    spacing = 12
    spread = s.height + spacing
    x = s.left - spread
    while x <= s.right + spread:
        _clipped(s, x, s.top, 1, 1)
        _clipped(s, x, s.bottom, 1, -1)
        x += spacing
    for x, y in ((s.left + 5, s.top + 17), (s.left + 45, s.top + 72), (s.left + 10, s.top + 128)):
        s.slot(x, y, 35)


def diagonal_guides(s: Scene, p: dict):
    band = s.height / 4
    for i in range(4):
        top = s.top + i * band
        bottom = top + band
        s.line(s.left, bottom, s.right, top, "light")
        if i:
            s.line(s.left, top, s.right, top, "normal")
        s.slot(s.left + 5, top + 15, 40)


def radial_polar(s: Scene, p: dict):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    s.radial(cx, cy, [12, 24, 36, 48], 12, "light")
    for x, y in ((cx - 17, cy - 4), (cx + 17, cy - 17), (cx - 33, cy + 26), (cx + 14, cy + 37)):
        s.slot(x, y, 24)


def coordinate_grid(s: Scene, p: dict):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    s.line(s.left + 4, cy, s.right - 4, cy, "strong")
    s.line(cx, s.top + 4, cx, s.bottom - 4, "strong")
    for delta in range(10, 61, 10):
        for sign in (-1, 1):
            x = cx + sign * delta
            if s.left + 3 < x < s.right - 3:
                s.line(x, cy - 2, x, cy + 2, "normal")
    for delta in range(10, 91, 10):
        for sign in (-1, 1):
            y = cy + sign * delta
            if s.top + 3 < y < s.bottom - 3:
                s.line(cx - 2, y, cx + 2, y, "normal")
    s.polyline([(s.right - 9, cy - 3), (s.right - 4, cy), (s.right - 9, cy + 3)], "strong")
    s.polyline([(cx - 3, s.top + 9), (cx, s.top + 4), (cx + 3, s.top + 9)], "strong")
    for x, y in ((cx + 7, cy - 22), (cx - 45, cy - 22), (cx - 45, cy + 24), (cx + 7, cy + 24)):
        s.slot(x, y, 35)


BUILDERS = {
    "triangular-grid": triangular_grid,
    "hex-grid": hex_grid,
    "rhombus-grid": rhombus_grid,
    "diagonal-guides": diagonal_guides,
    "radial-polar": radial_polar,
    "coordinate-grid": coordinate_grid,
}

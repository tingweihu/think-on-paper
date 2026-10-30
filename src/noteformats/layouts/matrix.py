from __future__ import annotations

from ..geometry import Scene


def quadrant_center_circle(s: Scene, p: dict):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    s.line(cx, s.top, cx, cy - 17, "normal")
    s.line(cx, cy + 17, cx, s.bottom, "normal")
    s.line(s.left, cy, cx - 17, cy, "normal")
    s.line(cx + 17, cy, s.right, cy, "normal")
    s.circle(cx, cy, 17, "normal")
    s.slot(cx - 12, cy + 1, 24)
    for x, y in ((s.left + 4, s.top + 16), (cx + 4, s.top + 16), (s.left + 4, cy + 20), (cx + 4, cy + 20)):
        s.slot(x, y, s.width / 2 - 8)


def matrix_2x3(s: Scene, p: dict):
    s.grid(s.left, s.top, s.width, s.height, 3, 2, "normal")
    w, h = s.width / 3, s.height / 2
    for row in range(2):
        for col in range(3):
            s.slot(s.left + col * w + 3, s.top + row * h + 16, w - 6)


def quadrant_rings(s: Scene, p: dict):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    r = 48
    for radius in (24, r):
        s.circle(cx, cy, radius, "light")
    s.line(cx - r, cy, cx + r, cy, "normal")
    s.line(cx, cy - r, cx, cy + r, "normal")
    for x, y in ((cx - 36, cy - 19), (cx + 10, cy - 19), (cx - 36, cy + 26), (cx + 10, cy + 26)):
        s.slot(x, y, 22)


BUILDERS = {
    "quadrant-center-circle": quadrant_center_circle,
    "matrix-2x3": matrix_2x3,
    "quadrant-rings": quadrant_rings,
}

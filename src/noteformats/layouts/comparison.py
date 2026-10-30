from __future__ import annotations

from math import cos, pi, sin

from ..geometry import Scene


def t_comparison(s: Scene, p: dict):
    head = s.top + 27
    cx = (s.left + s.right) / 2
    s.line(s.left, head, s.right, head, "normal")
    s.line(cx, head, cx, s.bottom, "normal")
    s.slot(s.left + 4, s.top + 16, s.width - 8)
    s.slot(s.left + 4, head + 18, s.width / 2 - 8)
    s.slot(cx + 4, head + 18, s.width / 2 - 8)


def three_way_comparison(s: Scene, p: dict):
    head = s.top + 28
    col = s.width / 3
    s.line(s.left, head, s.right, head, "normal")
    for n in (1, 2):
        x = s.left + n * col
        s.line(x, head, x, s.bottom, "normal")
    s.slot(s.left + 4, s.top + 16, s.width - 8)
    for n in range(3):
        s.slot(s.left + n * col + 3, head + 17, col - 6)


def venn_two(s: Scene, p: dict):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    s.circle(cx - 20, cy, 35, "normal")
    s.circle(cx + 20, cy, 35, "normal")
    s.slot(cx - 43, cy + 3, 22)
    s.slot(cx - 10, cy + 3, 20)
    s.slot(cx + 23, cy + 3, 22)


def venn_three(s: Scene, p: dict):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    for x, y in ((cx - 20, cy - 15), (cx + 20, cy - 15), (cx, cy + 19)):
        s.circle(x, y, 30, "normal")
    s.slot(cx - 35, cy - 19, 16)
    s.slot(cx + 22, cy - 19, 16)
    s.slot(cx - 8, cy + 35, 16)
    s.slot(cx - 7, cy - 18, 14)  # first and second only
    s.slot(cx - 19, cy + 13, 14)  # first and third only
    s.slot(cx + 5, cy + 13, 14)  # second and third only
    s.slot(cx - 10, cy + 1, 20)


def double_bubble(s: Scene, p: dict):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    left_x, right_x = cx - 22, cx + 22
    for x in (left_x, right_x):
        s.circle(x, cy, 14, "normal")
    s.slot(left_x - 10, cy + 2, 20)
    s.slot(right_x - 10, cy + 2, 20)
    for x, y in ((cx, cy - 39), (cx, cy + 39)):
        s.circle(x, y, 13, "normal")
        s.line(left_x + 7, cy + (-12 if y < cy else 12), x - 8, y + (9 if y < cy else -9), "light")
        s.line(right_x - 7, cy + (-12 if y < cy else 12), x + 8, y + (9 if y < cy else -9), "light")
        s.slot(x - 8, y + 2, 16)
    for x, side in ((left_x - 25, -1), (right_x + 25, 1)):
        s.circle(x, cy, 9, "normal")
        s.line(x - side * 9, cy, (left_x if side < 0 else right_x) + side * 14, cy, "light")
        s.slot(x - 7, cy + 2, 14)


def bridge_analogy(s: Scene, p: dict):
    cy = (s.top + s.bottom) / 2
    box_w, box_h = 37, 53
    lx, rx = s.left, s.right - box_w
    s.rect(lx, cy - box_h / 2, box_w, box_h, "normal")
    s.rect(rx, cy - box_h / 2, box_w, box_h, "normal")
    s.slot(lx + 3, cy - 7, box_w - 6)
    s.slot(rx + 3, cy - 7, box_w - 6)
    bx1, bx2 = lx + box_w, rx
    for y in (cy - 10, cy + 10):
        s.line(bx1, y, bx2, y, "normal")
    for n in range(3):
        x = bx1 + (bx2 - bx1) * (n + 1) / 4
        s.line(x, cy - 10, x, cy + 10, "light")
        s.slot(x - 5, cy + 2, 10)


BUILDERS = {
    "t-comparison": t_comparison,
    "three-way-comparison": three_way_comparison,
    "venn-two": venn_two,
    "venn-three": venn_three,
    "double-bubble": double_bubble,
    "bridge-analogy": bridge_analogy,
}

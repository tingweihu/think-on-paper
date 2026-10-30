from __future__ import annotations

from ..geometry import Scene


def blank(s: Scene, p: dict):
    s.slot(s.left + 4, s.top + 24, s.width - 8)
    s.slot(s.left + 4, s.top + 45, s.width - 8)
    s.slot(s.left + 4, s.top + 66, s.width - 8)


def ruled_double(s: Scene, p: dict):
    y = s.top + 7
    while y + 5 < s.bottom:
        s.line(s.left, y, s.right, y, "light")
        s.line(s.left, y + 5, s.right, y + 5, "normal")
        y += 13
    for y in (s.top + 11, s.top + 37, s.top + 63):
        s.slot(s.left + 2, y, s.width - 4)


def ruled_segmented(s: Scene, p: dict):
    gap = 5
    part = (s.width - gap * 2) / 3
    y = s.top + 8
    while y < s.bottom - 2:
        for col in range(3):
            x = s.left + col * (part + gap)
            s.line(x, y, x + part, y, "light")
        y += 8
    for col in range(3):
        s.slot(s.left + col * (part + gap) + 1, s.top + 14, part - 2)


def ruled_margin(s: Scene, p: dict):
    margin_x = s.left + 20
    s.line(margin_x, s.top, margin_x, s.bottom, "normal")
    y = s.top + 8
    while y < s.bottom - 1:
        s.line(s.left, y, s.right, y, "light")
        y += 8
    s.slot(s.left + 2, s.top + 15, 16)
    s.slot(margin_x + 3, s.top + 15, s.right - margin_x - 5)
    s.slot(margin_x + 3, s.top + 47, s.right - margin_x - 5)


def ruled_sketch_top(s: Scene, p: dict):
    split = s.top + s.height * 0.43
    s.line(s.left, split, s.right, split, "normal")
    y = split + 8
    while y < s.bottom - 1:
        s.line(s.left, y, s.right, y, "light")
        y += 8
    s.slot(s.left + 3, s.top + 15, s.width - 6)
    s.slot(s.left + 3, split + 15, s.width - 6)
    s.slot(s.left + 3, split + 39, s.width - 6)


BUILDERS = {
    "blank": blank,
    "ruled-double": ruled_double,
    "ruled-segmented": ruled_segmented,
    "ruled-margin": ruled_margin,
    "ruled-sketch-top": ruled_sketch_top,
}

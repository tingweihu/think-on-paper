from __future__ import annotations

from ..geometry import Scene


def two_equal_columns(s: Scene, p: dict):
    x = (s.left + s.right) / 2
    s.line(x, s.top, x, s.bottom, "normal")
    s.slot(s.left + 4, s.top + 18, s.width / 2 - 8)
    s.slot(x + 4, s.top + 18, s.width / 2 - 8)


def two_left_narrow(s: Scene, p: dict):
    x = s.left + s.width * 0.31
    s.line(x, s.top, x, s.bottom, "normal")
    s.slot(s.left + 3, s.top + 16, x - s.left - 6)
    s.slot(x + 4, s.top + 16, s.right - x - 8)


def three_columns(s: Scene, p: dict):
    w = s.width / 3
    for n in (1, 2):
        s.line(s.left + w * n, s.top, s.left + w * n, s.bottom, "normal")
    for n in range(3):
        s.slot(s.left + w * n + 3, s.top + 16, w - 6)


def column_dot_main(s: Scene, p: dict):
    x = s.left + 31
    s.line(x, s.top, x, s.bottom, "normal")
    y = s.top + 9
    while y < s.bottom - 1:
        s.line(s.left, y, x - 2, y, "light")
        y += 9
    gap, size = p["default_spacing_mm"]["dot"], p["dot_diameter_mm"]
    radius = size / 2
    for row in range(int((s.height - 2 * radius) / gap) + 1):
        for col in range(int((s.right - x - 3 - 2 * radius) / gap) + 1):
            s.dot(x + 3 + radius + col * gap, s.top + radius + row * gap, size, "light")
    s.slot(s.left + 2, s.top + 16, 26)
    s.slot(x + 7, s.top + 21, s.right - x - 13)
    s.slot(x + 7, s.top + 60, s.right - x - 13)


def two_columns_summary(s: Scene, p: dict):
    summary = s.bottom - 34
    x = (s.left + s.right) / 2
    s.line(x, s.top, x, summary, "normal")
    s.line(s.left, summary, s.right, summary, "normal")
    s.slot(s.left + 4, s.top + 16, s.width / 2 - 8)
    s.slot(x + 4, s.top + 16, s.width / 2 - 8)
    s.slot(s.left + 4, summary + 11, s.width - 8)


BUILDERS = {
    "two-equal-columns": two_equal_columns,
    "two-left-narrow": two_left_narrow,
    "three-columns": three_columns,
    "column-dot-main": column_dot_main,
    "two-columns-summary": two_columns_summary,
}

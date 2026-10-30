from __future__ import annotations

from ..geometry import Scene


def ruled_standard(s: Scene, p: dict):
    gap = p["default_spacing_mm"]["ruled"]
    y = s.top + gap
    while y < s.bottom - 1:
        s.line(s.left, y, s.right, y, "light")
        y += gap
    for n in (2, 5, 8, 11):
        s.slot(s.left + 2, s.top + gap * n - 1.7, s.width - 5)


def cornell(s: Scene, p: dict):
    x = s.left + s.width * 0.28
    summary = s.bottom - 32
    s.line(x, s.top, x, summary, "normal")
    s.line(s.left, summary, s.right, summary, "normal")
    gap = p["default_spacing_mm"]["ruled"]
    y = s.top + gap
    while y < summary - 2:
        s.line(x + 2, y, s.right, y, "light")
        y += gap
    s.slot(s.left + 2, s.top + 13, x - s.left - 3)
    s.slot(x + 3, s.top + 13, s.right - x - 5)
    s.slot(s.left + 2, summary + 9, s.width - 5)


def quadrant(s: Scene, p: dict):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    s.line(cx, s.top, cx, s.bottom, "normal")
    s.line(s.left, cy, s.right, cy, "normal")
    for x in (s.left + 4, cx + 4):
        for y in (s.top + 12, cy + 12):
            s.slot(x, y, s.width / 2 - 8)


def mandala_3x3(s: Scene, p: dict):
    size = min(s.width, s.height * 0.72)
    x = s.left + (s.width - size) / 2
    y = s.top + (s.height - size) / 2
    s.grid(x, y, size, size, 3, 3, "normal")
    cell = size / 3
    for row in range(3):
        for col in range(3):
            s.slot(x + col * cell + 3, y + row * cell + 11, cell - 6)


def fishbone(s: Scene, p: dict):
    cy = (s.top + s.bottom) / 2
    start, end = s.left + 10, s.right - 7
    s.line(start, cy, end, cy, "strong")
    s.polyline([(end - 7, cy - 5), (end, cy), (end - 7, cy + 5)], "strong")
    for i, frac in enumerate((0.2, 0.42, 0.64)):
        x = start + (end - start) * frac
        s.line(x, cy, x - 13, cy - 29, "normal")
        s.line(x, cy, x - 13, cy + 29, "normal")
        s.line(x - 22, cy - 29, x - 7, cy - 29, "light")
        s.line(x - 22, cy + 29, x - 7, cy + 29, "light")
        s.slot(x - 22, cy - 33, 22)
        s.slot(x - 22, cy + 38, 22)
    s.slot(end - 25, cy - 7, 25)


def storyboard_6(s: Scene, p: dict):
    gap_x, gap_y = 6, 6
    cell_w = (s.width - gap_x) / 2
    cell_h = (s.height - 2 * gap_y) / 3
    note_h = 11
    for row in range(3):
        for col in range(2):
            x = s.left + col * (cell_w + gap_x)
            y = s.top + row * (cell_h + gap_y)
            s.rect(x, y, cell_w, cell_h - note_h, "normal")
            s.line(x, y + cell_h - note_h + 3, x + cell_w, y + cell_h - note_h + 3, "light")
            s.slot(x + 3, y + cell_h - 3.3, cell_w - 6)


BUILDERS = {
    "ruled-standard": ruled_standard,
    "cornell": cornell,
    "quadrant": quadrant,
    "mandala-3x3": mandala_3x3,
    "fishbone": fishbone,
    "storyboard-6": storyboard_6,
}

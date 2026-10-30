from __future__ import annotations

from ..geometry import Scene


def _grid(s, x, y, w, h, gap, layer="light"):
    cols, rows = int(w / gap), int(h / gap)
    for c in range(cols + 1):
        xx = x + c * gap
        s.line(xx, y, xx, y + rows * gap, layer)
    for r in range(rows + 1):
        yy = y + r * gap
        s.line(x, yy, x + cols * gap, yy, layer)


def grid_standard(s: Scene, p: dict):
    gap = p["default_spacing_mm"]["grid"]
    _grid(s, s.left, s.top, s.width, s.height, gap)
    for x, y in ((s.left + 4, s.top + 10), (s.left + 39, s.top + 45), (s.left + 4, s.top + 85)):
        s.slot(x, y, 35)


def dot_standard(s: Scene, p: dict):
    gap, size = p["default_spacing_mm"]["dot"], p["dot_diameter_mm"]
    radius = size / 2
    for row in range(int((s.height - 2 * radius) / gap) + 1):
        for col in range(int((s.width - 2 * radius) / gap) + 1):
            s.dot(s.left + radius + col * gap, s.top + radius + row * gap, size, "light")
    for x, y in ((s.left + 5, s.top + 14), (s.left + 5, s.top + 49), (s.left + 5, s.top + 84)):
        s.slot(x, y, s.width - 10)


def dot_staggered(s: Scene, p: dict):
    gap, size = p["default_spacing_mm"]["dot"], p["dot_diameter_mm"]
    row_gap = gap * 0.8660254
    radius = size / 2
    for row in range(int((s.height - 2 * radius) / row_gap) + 1):
        x_offset = gap / 2 if row % 2 else 0
        for col in range(int((s.width - 2 * radius - x_offset) / gap) + 1):
            s.dot(s.left + radius + x_offset + col * gap, s.top + radius + row * row_gap, size, "light")
    for x, y in ((s.left + 5, s.top + 14), (s.left + 5, s.top + 49), (s.left + 5, s.top + 84)):
        s.slot(x, y, s.width - 10)


def grid_hierarchical(s: Scene, p: dict):
    # A distinct overview/detail topology: coarse full page; fine grid only in
    # the center overview cell cluster, rather than line-weight variants.
    coarse = 25
    cols, rows = int(s.width / coarse), int(s.height / coarse)
    base_x = s.left + (s.width - cols * coarse) / 2
    base_y = s.top + (s.height - rows * coarse) / 2
    s.grid(base_x, base_y, cols * coarse, rows * coarse, cols, rows, "normal")
    x, y = base_x + coarse, base_y + coarse
    _grid(s, x, y, coarse * 2, coarse * 3, 5, "light")
    s.slot(base_x + 3, base_y + 12, 20)
    s.slot(x + 3, y + 12, 44)
    s.slot(base_x + 3, base_y + coarse * 5 + 12, 20)


def dot_grid_split(s: Scene, p: dict):
    mid = (s.left + s.right) / 2
    gap, size = 5, p["dot_diameter_mm"]
    radius = size / 2
    s.line(mid, s.top, mid, s.bottom, "normal")
    for row in range(int((s.height - 2 * radius) / gap) + 1):
        for col in range(int((mid - s.left - 2 - 2 * radius) / gap) + 1):
            s.dot(s.left + radius + col * gap, s.top + radius + row * gap, size, "light")
    _grid(s, mid + 2, s.top, s.right - mid - 2, s.height, gap)
    s.slot(s.left + 5, s.top + 15, mid - s.left - 10)
    s.slot(mid + 5, s.top + 15, s.right - mid - 10)


BUILDERS = {
    "grid-standard": grid_standard,
    "dot-standard": dot_standard,
    "dot-staggered": dot_staggered,
    "grid-hierarchical": grid_hierarchical,
    "dot-grid-split": dot_grid_split,
}

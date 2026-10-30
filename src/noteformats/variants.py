"""Stable variant IDs and their reproducible geometry.

Each entry is (classification, operation, parameter).  The original target and
reason remain in content/merged.json.  Equivalent IDs deliberately share blank
geometry; parameter variants and independent restorations do not.
"""

from __future__ import annotations

import json
from math import cos, pi, sin
from pathlib import Path

from .geometry import Scene, Shape

ORIGINAL_MERGES = json.loads((Path(__file__).resolve().parents[2] / "content" / "merged.json").read_text(encoding="utf-8"))

# "independent" restores a candidate whose main writing action is not supplied
# by the old target.  Two old independent header layouts are reviewed below.
RECLASSIFIED_HEADERS = {
    "t-comparison": "two-equal-columns",
    "three-way-comparison": "three-columns",
}

VARIANT_METHODS = {
    "ruled-narrow": ("parameter", "ruled", 5.5),
    "ruled-wide": ("parameter", "ruled", 10),
    "grid-fine": ("parameter", "grid", 3),
    "grid-large": ("parameter", "grid", 8),
    "dot-fine": ("parameter", "dot", 3.5),
    "cornell-mirrored": ("parameter", "mirror_x", None),
    "fishbone-four": ("parameter", "fishbone", 2),
    "storyboard-three": ("parameter", "storyboard", 3),
    "storyboard-four": ("parameter", "storyboard", 4),
    "isometric-grid": ("equivalent", "copy", None),
    "engineering-grid": ("parameter", "engineering_grid", 5),
    "two-right-narrow": ("parameter", "mirror_x", None),
    "three-stacked-cards": ("parameter", "stacked_cards", 3),
    "six-cards": ("parameter", "card_grid", 6),
    "eight-cards": ("parameter", "card_grid", 8),
    "mirrored-compare-cards": ("equivalent", "copy", None),
    "cross-compare": ("equivalent", "copy", None),
    "matrix-3x2": ("parameter", "matrix", (2, 3)),
    "matrix-3x3": ("independent", "matrix", (3, 3)),
    "axis-matrix": ("equivalent", "copy", None),
    "weighted-matrix": ("parameter", "weighted_matrix", None),
    "flower-six": ("parameter", "flower", 6),
    "flow-five-vertical": ("parameter", "vertical_flow", 5),
    "cycle-six": ("parameter", "cycle", 6),
    "causal-chain": ("equivalent", "copy", None),
    "problem-solution-three": ("independent", "diverging_flow", 3),
    "five-why-chain": ("equivalent", "vertical_flow", 5),
    "root-cause-tree": ("independent", "root_cause_tree", None),
    "mindmap-eight": ("parameter", "mindmap", 8),
    "bottom-up-tree": ("parameter", "mirror_y", None),
    "pyramid-five": ("parameter", "pyramid", 5),
    "frayer": ("equivalent", "copy", None),
    "cue-answer": ("equivalent", "copy", None),
    "recall-strip": ("parameter", "recall_strip", None),
    "concept-examples-six": ("equivalent", "copy", None),
    "quote-side-notes": ("equivalent", "copy", None),
    "quote-comment-parallel": ("equivalent", "copy", None),
    "observation-interpretation": ("equivalent", "copy", None),
    "source-large-plus-cards": ("equivalent", "copy", None),
    "research-index-cards": ("equivalent", "copy", None),
    "crazy-eight": ("parameter", "card_grid", 8),
    "idea-bubbles-six": ("parameter", "flower", 6),
    "hero-idea-seven-variations": ("parameter", "center_satellites", 7),
    "dual-input-synthesis": ("parameter", "converging_flow", 2),
    "seven-ideation-cards": ("parameter", "card_grid", 7),
    "two-sketch-notes": ("parameter", "storyboard", 2),
    "mixed-storyboard": ("parameter", "mixed_storyboard", None),
    "pixel-stitch-grid": ("equivalent", "copy", None),
    "ruled-and-sketch": ("parameter", "ruled_sketch_bottom", None),
}

if set(VARIANT_METHODS) != set(ORIGINAL_MERGES):
    raise RuntimeError("Every stable variant ID needs one classification")


def _mirror(s: Scene, axis: str) -> None:
    mx = lambda x: s.left + s.right - x
    my = lambda y: s.top + s.bottom - y
    result = []
    for shape in s.shapes:
        v = shape.values
        if shape.kind == "line":
            values = (mx(v[0]), v[1], mx(v[2]), v[3]) if axis == "x" else (v[0], my(v[1]), v[2], my(v[3]))
        elif shape.kind == "rect":
            values = (mx(v[0] + v[2]), v[1], v[2], v[3]) if axis == "x" else (v[0], my(v[1] + v[3]), v[2], v[3])
        elif shape.kind in ("circle", "dot"):
            values = (mx(v[0]), v[1], v[2]) if axis == "x" else (v[0], my(v[1]), v[2])
        else:
            values = tuple((mx(value) if axis == "x" and n % 2 == 0 else my(value) if axis == "y" and n % 2 else value) for n, value in enumerate(v))
        result.append(Shape(shape.kind, values, shape.layer))
    s.shapes = result
    s.slots = [(mx(x + w), y, w) if axis == "x" else (x, my(y), w) for x, y, w in s.slots]


def _grid(s: Scene, gap: float, engineering: bool = False):
    cols, rows = int(s.width / gap), int(s.height / gap)
    for c in range(cols + 1):
        x = s.left + c * gap
        s.line(x, s.top, x, s.top + rows * gap, "normal" if engineering and c % 5 == 0 else "light")
    for r in range(rows + 1):
        y = s.top + r * gap
        s.line(s.left, y, s.left + cols * gap, y, "normal" if engineering and r % 5 == 0 else "light")
    for x, y in ((s.left + 4, s.top + 10), (s.left + 39, s.top + 45), (s.left + 4, s.top + 85)):
        s.slot(x, y, 35)


def _dot(s: Scene, p: dict, gap: float):
    radius = p["dot_diameter_mm"] / 2
    for row in range(int((s.height - 2 * radius) / gap) + 1):
        for col in range(int((s.width - 2 * radius) / gap) + 1):
            s.dot(s.left + radius + col * gap, s.top + radius + row * gap, p["dot_diameter_mm"], "light")
    for y in (s.top + 14, s.top + 49, s.top + 84):
        s.slot(s.left + 5, y, s.width - 10)


def _storyboard(s: Scene, n: int):
    cols = 1 if n in (2, 3) else 2
    rows = (n + cols - 1) // cols
    gap_x, gap_y = 6, 6
    w = (s.width - (cols - 1) * gap_x) / cols
    h = (s.height - (rows - 1) * gap_y) / rows
    for i in range(n):
        x = s.left + (i % cols) * (w + gap_x)
        y = s.top + (i // cols) * (h + gap_y)
        s.rect(x, y, w, h - 11, "normal")
        s.line(x, y + h - 8, x + w, y + h - 8, "light")
        s.slot(x + 3, y + h - 3, w - 6)


def _cards(s: Scene, n: int, stacked: bool = False):
    cols = 1 if stacked else 2
    rows = (n + cols - 1) // cols
    gap = 6
    w = (s.width - (cols - 1) * gap) / cols
    h = (s.height - (rows - 1) * gap) / rows
    for i in range(n):
        x = s.left + (i % cols) * (w + gap)
        if n % 2 and i == n - 1 and not stacked:
            x = s.left + (s.width - w) / 2
        y = s.top + (i // cols) * (h + gap)
        s.rect(x, y, w, h, "normal")
        s.slot(x + 3, y + min(16, h / 2), w - 6)


def _matrix(s: Scene, cols: int, rows: int):
    s.grid(s.left, s.top, s.width, s.height, cols, rows, "normal")
    w, h = s.width / cols, s.height / rows
    for row in range(rows):
        for col in range(cols):
            s.slot(s.left + col * w + 3, s.top + row * h + min(16, h / 2), w - 6)


def _arrow(s: Scene, a: tuple[float, float], b: tuple[float, float]):
    from .layouts.flow import arrow
    arrow(s, *a, *b, "light")


def _vertical_flow(s: Scene, n: int):
    w, h = 74, 26
    gap = (s.height - n * h) / (n - 1)
    x = s.left + (s.width - w) / 2
    for i in range(n):
        y = s.top + i * (h + gap)
        s.rect(x, y, w, h, "normal")
        s.slot(x + 4, y + 16, w - 8)
        if i < n - 1:
            _arrow(s, (x + w / 2, y + h + 1), (x + w / 2, y + h + gap - 1))


def _cycle(s: Scene, n: int):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    pts = [(cx + 42 * cos(-pi / 2 + 2 * pi * i / n), cy + 64 * sin(-pi / 2 + 2 * pi * i / n)) for i in range(n)]
    for i, (x, y) in enumerate(pts):
        s.circle(x, y, 10, "normal")
        s.slot(x - 7, y + 2, 14)
        xx, yy = pts[(i + 1) % n]
        dx, dy = xx - x, yy - y
        length = (dx * dx + dy * dy) ** .5
        _arrow(s, (x + dx * 12 / length, y + dy * 12 / length), (xx - dx * 12 / length, yy - dy * 12 / length))


def _converging(s: Scene, n: int, diverge: bool = False):
    left_x, right_x = s.left + 2, s.right - 40
    ys = [s.top + 16 + i * (s.height - 32 - 26) / max(1, n - 1) for i in range(n)]
    mid_y = (s.top + s.bottom - 40) / 2
    if diverge:
        s.rect(left_x, mid_y, 38, 40, "strong")
        s.slot(left_x + 4, mid_y + 22, 30)
        for y in ys:
            s.rect(right_x, y, 38, 26, "normal")
            s.slot(right_x + 3, y + 16, 32)
            _arrow(s, (left_x + 40, mid_y + 20), (right_x - 2, y + 13))
    else:
        for y in ys:
            s.rect(left_x, y, 38, 26, "normal")
            s.slot(left_x + 3, y + 16, 32)
            _arrow(s, (left_x + 40, y + 13), (right_x - 2, mid_y + 20))
        s.rect(right_x, mid_y, 38, 40, "strong")
        s.slot(right_x + 4, mid_y + 22, 30)


def _mindmap(s: Scene, n: int):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    s.circle(cx, cy, 17, "strong")
    s.slot(cx - 12, cy + 2, 24)
    for i in range(n):
        a = -pi / 2 + i * 2 * pi / n
        ux, uy = cos(a), sin(a)
        x, y = cx + 44 * ux, cy + 65 * uy
        s.line(cx + 18 * ux, cy + 18 * uy, x - 11 * ux, y - 11 * uy, "light")
        s.circle(x, y, 10, "normal")
        s.slot(x - 7, y + 2, 14)


def _flower(s: Scene, n: int):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    s.circle(cx, cy, 16, "normal")
    s.slot(cx - 10, cy + 2, 20)
    for i in range(n):
        a = -pi / 2 + i * 2 * pi / n
        x, y = cx + 35 * cos(a), cy + 35 * sin(a)
        s.circle(x, y, 16, "light")
        s.slot(x - 10, y + 2, 20)


def _fishbone(s: Scene, branches_per_side: int):
    cy = (s.top + s.bottom) / 2
    start, end = s.left + 10, s.right - 7
    s.line(start, cy, end, cy, "strong")
    s.polyline([(end - 7, cy - 5), (end, cy), (end - 7, cy + 5)], "strong")
    for i in range(branches_per_side):
        x = start + (end - start) * (i + 1) / (branches_per_side + 1)
        for sign in (-1, 1):
            yy = cy + sign * 29
            s.line(x, cy, x - 13, yy, "normal")
            s.line(x - 22, yy, x - 7, yy, "light")
            s.slot(x - 22, yy + (7 if sign > 0 else -4), 22)
    s.slot(end - 25, cy - 7, 25)


def _root_cause(s: Scene):
    top = s.top + 9
    leaves = [s.left + 15 + i * (s.width - 30) / 3 for i in range(4)]
    for x in leaves:
        s.rect(x - 12, top, 24, 27, "normal")
        s.slot(x - 10, top + 16, 20)
    middles = [s.left + 30, s.right - 30]
    mid_y = s.top + 79
    for j, x in enumerate(middles):
        s.rect(x - 17, mid_y, 34, 28, "normal")
        s.slot(x - 14, mid_y + 17, 28)
        for source in leaves[2 * j:2 * j + 2]:
            _arrow(s, (source, top + 29), (x, mid_y - 2))
    output_y = s.bottom - 43
    cx = (s.left + s.right) / 2
    s.rect(cx - 27, output_y, 54, 35, "strong")
    s.slot(cx - 23, output_y + 20, 46)
    for x in middles:
        _arrow(s, (x, mid_y + 30), (cx, output_y - 2))


def _pyramid(s: Scene, n: int):
    cx = (s.left + s.right) / 2
    top, bottom = s.top + 7, s.bottom - 7
    half = s.width * .44
    s.polyline([(cx, top), (cx + half, bottom), (cx - half, bottom)], "strong", closed=True)
    for i in range(1, n):
        y = top + (bottom - top) * i / n
        hw = half * i / n
        s.line(cx - hw, y, cx + hw, y, "normal")
    for i in range(n):
        y = top + (bottom - top) * (i + .72) / n
        width = max(12, 2 * half * (i + .72) / n - 6)
        s.slot(cx - width / 2, y, width)


def _build(layout_id: str, base_builders: dict, s: Scene, p: dict):
    category, operation, value = VARIANT_METHODS[layout_id]
    target = ORIGINAL_MERGES[layout_id]["target"]
    if operation == "copy":
        base_builders[target](s, p)
    elif operation in ("mirror_x", "mirror_y"):
        base_builders[target](s, p)
        _mirror(s, operation[-1])
    elif operation == "ruled":
        y = s.top + value
        while y < s.bottom - 1:
            s.line(s.left, y, s.right, y, "light")
            y += value
        for n in (2, 5, 8, 11):
            yy = s.top + value * n - 1.7
            if yy < s.bottom:
                s.slot(s.left + 2, yy, s.width - 5)
    elif operation in ("grid", "engineering_grid"):
        _grid(s, value, operation == "engineering_grid")
    elif operation == "dot":
        _dot(s, p, value)
    elif operation == "fishbone":
        _fishbone(s, value)
    elif operation == "storyboard":
        _storyboard(s, value)
    elif operation == "stacked_cards":
        _cards(s, value, True)
    elif operation == "card_grid":
        _cards(s, value)
    elif operation == "matrix":
        _matrix(s, *value)
    elif operation == "weighted_matrix":
        x1 = s.left + s.width * .27
        x2 = s.left + s.width * .65
        y = s.top + s.height * .34
        s.rect(s.left, s.top, s.width, s.height, "normal")
        s.line(x1, s.top, x1, s.bottom, "normal")
        s.line(x2, s.top, x2, s.bottom, "normal")
        s.line(s.left, y, s.right, y, "normal")
        for xx, ww in ((s.left, x1 - s.left), (x1, x2 - x1), (x2, s.right - x2)):
            for yy, hh in ((s.top, y - s.top), (y, s.bottom - y)):
                s.slot(xx + 3, yy + min(16, hh / 2), ww - 6)
    elif operation == "flower":
        _flower(s, value)
    elif operation == "vertical_flow":
        _vertical_flow(s, value)
    elif operation == "cycle":
        _cycle(s, value)
    elif operation == "diverging_flow":
        _converging(s, value, True)
    elif operation == "converging_flow":
        _converging(s, value)
    elif operation == "root_cause_tree":
        _root_cause(s)
    elif operation == "mindmap":
        _mindmap(s, value)
    elif operation == "pyramid":
        _pyramid(s, value)
    elif operation == "recall_strip":
        base_builders[target](s, p)
        y = s.bottom - 16
        s.line(s.left, y, s.right, y, "strong")
        s.slot(s.left + 3, y + 10, s.width - 6)
    elif operation == "center_satellites":
        cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
        s.rect(cx - 17, cy - 17, 34, 34, "strong")
        s.slot(cx - 14, cy + 2, 28)
        for i in range(value):
            a = -pi / 2 + i * 2 * pi / value
            x, y = cx + 43 * cos(a), cy + 68 * sin(a)
            s.rect(x - 13, y - 12, 26, 24, "normal")
            s.slot(x - 11, y + 2, 22)
    elif operation == "mixed_storyboard":
        s.rect(s.left, s.top, s.width, 60, "normal")
        s.slot(s.left + 3, s.top + 72, s.width - 6)
        gap = 5
        w = (s.width - 2 * gap) / 3
        for i in range(3):
            x = s.left + i * (w + gap)
            s.rect(x, s.top + 84, w, 72, "normal")
            s.slot(x + 3, s.top + 167, w - 6)
    elif operation == "ruled_sketch_bottom":
        split = s.top + s.height * .57
        s.line(s.left, split, s.right, split, "normal")
        y = s.top + 8
        while y < split - 2:
            s.line(s.left, y, s.right, y, "light")
            y += 8
        s.slot(s.left + 3, s.top + 18, s.width - 6)
        s.slot(s.left + 3, split + 20, s.width - 6)
    else:
        raise RuntimeError(f"Unknown variant operation: {layout_id}: {operation}")
    if not s.bounds_ok():
        raise ValueError(f"Variant exceeds page: {layout_id}")


def make_variant_builders(base_builders: dict) -> dict:
    def builder_for(layout_id):
        def build(s, p):
            _build(layout_id, base_builders, s, p)
        build.__name__ = "variant_" + layout_id.replace("-", "_")
        return build
    return {layout_id: builder_for(layout_id) for layout_id in VARIANT_METHODS}

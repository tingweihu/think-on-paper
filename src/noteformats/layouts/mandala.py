from __future__ import annotations

from math import cos, pi, sin

from ..geometry import Scene


def mandala_9x9(s: Scene, p: dict):
    size = min(s.width, s.height * 0.72)
    x, y = s.left + (s.width - size) / 2, s.top + (s.height - size) / 2
    s.rect(x, y, size, size, "normal")
    cell = size / 9
    for n in range(1, 9):
        layer = "strong" if n % 3 == 0 else "light"
        s.line(x + n * cell, y, x + n * cell, y + size, layer)
        s.line(x, y + n * cell, x + size, y + n * cell, layer)
    for row in (1, 4, 7):
        for col in (1, 4, 7):
            s.slot(x + col * cell + 1, y + row * cell + 7, cell - 2)


def center_eight_boxes(s: Scene, p: dict):
    size, gap = 112, 5
    box = (size - gap * 2) / 3
    x, y = s.left + (s.width - size) / 2, s.top + (s.height - size) / 2
    for row in range(3):
        for col in range(3):
            xx, yy = x + col * (box + gap), y + row * (box + gap)
            s.rect(xx, yy, box, box, "strong" if (row, col) == (1, 1) else "normal")
            s.slot(xx + 3, yy + 13, box - 6)


def diamond_eight_rays(s: Scene, p: dict):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    r = 15
    s.polyline([(cx, cy-r), (cx+r, cy), (cx, cy+r), (cx-r, cy)], "normal", closed=True)
    s.slot(cx - 9, cy + 2, 18)
    for i in range(8):
        a = -pi/2 + i*pi/4
        ux, uy = cos(a), sin(a)
        start = (cx + 18*ux, cy + 18*uy)
        end = (cx + 49*ux, cy + 49*uy)
        s.line(*start, *end, "light")
        tx, ty = -uy, ux
        s.line(end[0]-7*tx, end[1]-7*ty, end[0]+7*tx, end[1]+7*ty, "light")
        s.slot(end[0]-9, end[1]-4, 18)


def flower_eight(s: Scene, p: dict):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    s.circle(cx, cy, 16, "normal")
    s.slot(cx - 10, cy + 2, 20)
    for i in range(8):
        a = -pi/2 + i*pi/4
        x, y = cx + 31*cos(a), cy + 31*sin(a)
        s.circle(x, y, 17, "light")
        s.slot(x - 10, y + 2, 20)


def flower_two_rings(s: Scene, p: dict):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    s.circle(cx, cy, 11, "normal")
    s.slot(cx - 8, cy + 2, 16)
    for radius in (25, 46):
        for i in range(6):
            a = -pi/2 + i*pi/3
            x, y = cx + radius*cos(a), cy + radius*sin(a)
            s.circle(x, y, 11, "light")
            s.slot(x - 8, y + 2, 16)


def mandala_extended(s: Scene, p: dict):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    size = 78
    x, y = cx - size / 2, cy - size / 2
    s.grid(x, y, size, size, 3, 3, "normal")
    cell = size / 3
    for row in range(3):
        for col in range(3):
            s.slot(x + col*cell + 3, y + row*cell + 11, cell - 6)
    side_w, side_h = 17, 34
    for xx in (s.left, s.right - side_w):
        s.rect(xx, cy - side_h/2, side_w, side_h, "light")
        s.slot(xx + 2, cy + 2, side_w - 4)
    for yy in (s.top + 4, s.bottom - 24):
        s.rect(cx - 30, yy, 60, 20, "light")
        s.slot(cx - 26, yy + 12, 52)


BUILDERS = {
    "mandala-9x9": mandala_9x9,
    "center-eight-boxes": center_eight_boxes,
    "diamond-eight-rays": diamond_eight_rays,
    "flower-eight": flower_eight,
    "flower-two-rings": flower_two_rings,
    "mandala-extended": mandala_extended,
}

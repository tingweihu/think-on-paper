from __future__ import annotations

from dataclasses import dataclass, field
from math import cos, pi, sin


@dataclass(frozen=True)
class Shape:
    kind: str
    values: tuple[float, ...]
    layer: str = "normal"


@dataclass
class Scene:
    page_w: float
    page_h: float
    left: float
    top: float
    right: float
    bottom: float
    shapes: list[Shape] = field(default_factory=list)
    slots: list[tuple[float, float, float]] = field(default_factory=list)

    @classmethod
    def from_profile(cls, p: dict) -> Scene:
        w, h = p["page_mm"]
        m = p["safe_margin_mm"]
        return cls(w, h, m["left"], m["top"], w - m["right"], h - m["bottom"])

    @property
    def width(self) -> float:
        return self.right - self.left

    @property
    def height(self) -> float:
        return self.bottom - self.top

    def line(self, x1, y1, x2, y2, layer="normal"):
        self.shapes.append(Shape("line", (x1, y1, x2, y2), layer))

    def rect(self, x, y, w, h, layer="normal"):
        self.shapes.append(Shape("rect", (x, y, w, h), layer))

    def circle(self, x, y, r, layer="normal"):
        self.shapes.append(Shape("circle", (x, y, r), layer))

    def dot(self, x, y, diameter, layer="normal"):
        self.shapes.append(Shape("dot", (x, y, diameter / 2), layer))

    def polyline(self, points, layer="normal", closed=False):
        self.shapes.append(Shape("polygon" if closed else "polyline", tuple(v for pt in points for v in pt), layer))

    def grid(self, x, y, w, h, cols, rows, layer="normal", outline=True):
        if outline:
            self.rect(x, y, w, h, layer)
        for c in range(1, cols):
            xx = x + w * c / cols
            self.line(xx, y, xx, y + h, layer)
        for r in range(1, rows):
            yy = y + h * r / rows
            self.line(x, yy, x + w, yy, layer)

    def radial(self, cx, cy, radii, rays, layer="normal"):
        for r in radii:
            self.circle(cx, cy, r, layer)
        max_r = max(radii)
        for i in range(rays):
            a = -pi / 2 + 2 * pi * i / rays
            self.line(cx, cy, cx + max_r * cos(a), cy + max_r * sin(a), layer)

    def slot(self, x, y, width):
        self.slots.append((x, y, width))

    def bounds_ok(self, tolerance=0.02, safe=False):
        min_x, max_x = (self.left, self.right) if safe else (0, self.page_w)
        min_y, max_y = (self.top, self.bottom) if safe else (0, self.page_h)
        for s in self.shapes:
            if s.kind in ("line", "rect"):
                if s.kind == "line":
                    x1, y1, x2, y2 = s.values
                    points = [(x1, y1), (x2, y2)]
                else:
                    x, y, w, h = s.values
                    points = [(x, y), (x + w, y + h)]
            elif s.kind in ("circle", "dot"):
                x, y, r = s.values
                points = [(x - r, y - r), (x + r, y + r)]
            else:
                points = list(zip(s.values[::2], s.values[1::2]))
            for x, y in points:
                if not (min_x - tolerance <= x <= max_x + tolerance and min_y - tolerance <= y <= max_y + tolerance):
                    return False
        return True

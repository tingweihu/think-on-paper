from __future__ import annotations

from ..geometry import Scene


def two_stacked_cards(s: Scene, p: dict):
    gap = 8
    h = (s.height - gap) / 2
    for n in range(2):
        y = s.top + n * (h + gap)
        s.rect(s.left, y, s.width, h, "normal")
        s.slot(s.left + 5, y + 16, s.width - 10)


def four_cards(s: Scene, p: dict):
    gap = 7
    w, h = (s.width - gap) / 2, (s.height - gap) / 2
    for row in range(2):
        for col in range(2):
            x, y = s.left + col * (w + gap), s.top + row * (h + gap)
            s.rect(x, y, w, h, "normal")
            s.slot(x + 4, y + 16, w - 8)


def center_four_satellites(s: Scene, p: dict):
    cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
    center_w, center_h = s.width * 0.40, 38
    s.rect(cx - center_w / 2, cy - center_h / 2, center_w, center_h, "normal")
    s.slot(cx - center_w / 2 + 4, cy - 2, center_w - 8)
    top_w, top_h = 62, 28
    s.rect(cx - top_w / 2, s.top, top_w, top_h, "normal")
    s.line(cx, s.top + top_h, cx, cy - center_h / 2, "light")
    s.slot(cx - top_w / 2 + 4, s.top + 15, top_w - 8)
    s.rect(cx - top_w / 2, s.bottom - top_h, top_w, top_h, "normal")
    s.line(cx, cy + center_h / 2, cx, s.bottom - top_h, "light")
    s.slot(cx - top_w / 2 + 4, s.bottom - top_h + 15, top_w - 8)
    side_w, side_h = 25, 36
    for x in (s.left, s.right - side_w):
        s.rect(x, cy - side_h / 2, side_w, side_h, "normal")
        s.slot(x + 3, cy - 3, side_w - 6)
    s.line(s.left + side_w, cy, cx - center_w / 2, cy, "light")
    s.line(cx + center_w / 2, cy, s.right - side_w, cy, "light")


def hero_three_cards(s: Scene, p: dict):
    gap = 7
    hero_h = s.height * 0.55
    small_h = s.height - hero_h - gap
    small_w = (s.width - gap * 2) / 3
    s.rect(s.left, s.top, s.width, hero_h, "normal")
    s.slot(s.left + 5, s.top + 18, s.width - 10)
    for n in range(3):
        x = s.left + n * (small_w + gap)
        y = s.top + hero_h + gap
        s.rect(x, y, small_w, small_h, "normal")
        s.slot(x + 3, y + 15, small_w - 6)


def mosaic_cards(s: Scene, p: dict):
    gap = 6
    left_w = s.width * 0.55
    right_w = s.width - left_w - gap
    s.rect(s.left, s.top, left_w, s.height * 0.64, "normal")
    s.slot(s.left + 5, s.top + 18, left_w - 10)
    s.rect(s.left, s.top + s.height * 0.64 + gap, left_w, s.height * 0.36 - gap, "normal")
    s.slot(s.left + 5, s.top + s.height * 0.64 + gap + 16, left_w - 10)
    right_x = s.left + left_w + gap
    h = (s.height - gap) / 2
    for n in range(2):
        y = s.top + n * (h + gap)
        s.rect(right_x, y, right_w, h, "normal")
        s.slot(right_x + 4, y + 16, right_w - 8)


BUILDERS = {
    "two-stacked-cards": two_stacked_cards,
    "four-cards": four_cards,
    "center-four-satellites": center_four_satellites,
    "hero-three-cards": hero_three_cards,
    "mosaic-cards": mosaic_cards,
}

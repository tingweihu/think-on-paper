"""Original, editable teaching marks that appear only in example SVGs."""

from __future__ import annotations

from html import escape

from .geometry import Scene


def _line(x1, y1, x2, y2):
    return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}"/>'


def _rect(x, y, w, h):
    return f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}"/>'


def _circle(x, y, r):
    return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}"/>'


def _text(x, y, value, size=2.65):
    return f'<text x="{x:.2f}" y="{y:.2f}" fill="#514D47" stroke="none" font-family="Arial, sans-serif" font-size="{size:.2f}">{escape(value)}</text>'


def _person(x, y):
    return [_circle(x, y, 2.5), _line(x, y + 2.5, x, y + 13),
            _line(x - 5, y + 7, x + 5, y + 7), _line(x, y + 13, x - 4, y + 19),
            _line(x, y + 13, x + 4, y + 19)]


def _storyboard(s: Scene):
    gap_x, gap_y = 6, 6
    w, h = (s.width - gap_x) / 2, (s.height - 2 * gap_y) / 3
    parts = []
    for index in range(6):
        x = s.left + (index % 2) * (w + gap_x)
        y = s.top + (index // 2) * (h + gap_y)
        parts.append(_line(x + 5, y + 38, x + w - 5, y + 38))
        if index in (0, 5):
            parts += [_rect(x + 37, y + 8, 12, 30), _circle(x + 46, y + 23, .8)]
            parts += _person(x + (17 if index == 0 else 22), y + 16)
            if index == 5:
                parts.append(_rect(x + 25, y + 22, 7, 5))
        elif index in (1, 3):
            parts += [_rect(x + 6, y + 9, 31, 29)]
            parts += [_line(x + 6, y + yy, x + 37, y + yy) for yy in (18, 28)]
            parts += [_line(x + xx, y + 10, x + xx, y + 37) for xx in (15, 24, 32)]
            parts += _person(x + 48, y + 15)
            if index == 3:
                parts += [_rect(x + 25, y + 16, 5, 10), _line(x + 30, y + 21, x + 45, y + 22)]
        elif index == 2:
            parts += [_rect(x + 8, y + 12, 29, 19), _line(x + 12, y + 17, x + 32, y + 17),
                      _line(x + 12, y + 22, x + 28, y + 22), _line(x + 11, y + 31, x + 7, y + 38)]
            parts += _person(x + 48, y + 15)
        else:
            parts += [_line(x + 7, y + 30, x + 49, y + 30), _rect(x + 14, y + 25, 10, 5),
                      _rect(x + 32, y + 21, 8, 9)]
            parts += _person(x + 46, y + 11)
    return parts


def _music(s: Scene):
    y = s.top + 18
    # Quarter note, two beamed eighth notes, then a half note. The example
    # deliberately avoids assigning pitches without a clef.
    notes = [(s.left + 25, y + 10.8), (s.left + 49, y + 8.1),
             (s.left + 64, y + 5.4), (s.left + 91, y + 6.75)]
    parts = []
    for index, (x, yy) in enumerate(notes):
        parts.append(f'<ellipse cx="{x:.2f}" cy="{yy:.2f}" rx="2.25" ry="1.35" '
                     + ('fill="none" stroke-width="0.7"/>' if index == 3 else 'fill="#514D47" stroke="none"/>'))
        parts.append(_line(x + 2, yy, x + 2, yy - 17))
    parts += [_line(notes[1][0] + 2, notes[1][1] - 17, notes[2][0] + 2, notes[2][1] - 17),
              _line(notes[1][0] + 2, notes[1][1] - 15, notes[2][0] + 2, notes[2][1] - 15),
              _line(s.left + 111, y, s.left + 111, y + 10.8)]
    return parts


THREE_WAY = {
    "zh-TW": (("設備：投影", "交通：近", "費用：免"), ("設備：音響", "交通：中", "費用：低"), ("設備：無", "交通：遠", "費用：免")),
    "en": (("Gear: screen", "Travel: near", "Cost: free"), ("Gear: audio", "Travel: mid", "Cost: low"), ("Gear: none", "Travel: far", "Cost: free")),
    "ja": (("設備：画面", "交通：近い", "費用：無料"), ("設備：音響", "交通：中", "費用：低い"), ("設備：なし", "交通：遠い", "費用：無料")),
}


def _three_way(s: Scene, lang: str, header: bool):
    col = s.width / 3
    start = s.top + (62 if header else 38)
    parts = []
    for j, values in enumerate(THREE_WAY[lang]):
        x = s.left + j * col + 3
        for k, value in enumerate(values):
            parts.append(_text(x, start + k * 24, value, 2.55))
    return parts


FISHBONE_DETAILS = {
    "zh-TW": ("晚間", "訊息晚", "步驟多", "入口難找"),
    "en": ("Late hour", "Late notice", "Many steps", "Hidden link"),
    "ja": ("夜間", "案内が遅い", "手順が多い", "入口が不明"),
}


def _fishbone(s: Scene, lang: str):
    cy = (s.top + s.bottom) / 2
    start, end = s.left + 10, s.right - 7
    positions = [start + (end - start) * frac for frac in (.2, .42, .64)]
    parts = []
    for index, (x, sign) in enumerate(((positions[0], -1), (positions[1], -1),
                                       (positions[1], 1), (positions[2], 1))):
        yy = cy + sign * 15
        parts.append(_line(x - 6, yy, x + 2, yy - sign * 5))
        parts.append(_text(x - 13, yy - sign * 7, FISHBONE_DETAILS[lang][index], 2.2))
    return parts


MINDMAP_DETAILS = {
    "zh-TW": ("通道", "海報"), "en": ("Access", "Poster"), "ja": ("動線", "ポスター"),
}


def _mindmap(s: Scene, lang: str):
    cy = (s.top + s.bottom) / 2
    # Add second-level ideas to the Venue and Publicity branches.
    return [_line(s.right - 20, cy - 38, s.right - 8, cy - 59),
            _line(s.left + 20, cy - 38, s.left + 8, cy - 59),
            _text(s.right - 22, cy - 61, MINDMAP_DETAILS[lang][0], 2.35),
            _text(s.left + 1, cy - 61, MINDMAP_DETAILS[lang][1], 2.35)]


MANDA = {
    "zh-TW": ("場", "時", "書", "人", "材", "談", "預", "後"),
    "en": ("Venue", "Time", "Books", "People", "Items", "Talk", "Cost", "Next"),
    "ja": ("会場", "時間", "本", "参加", "資料", "討論", "予算", "次回"),
}


def _mandala(s: Scene, lang: str):
    size = min(s.width, s.height * .72)
    x = s.left + (s.width - size) / 2
    y = s.top + (s.height - size) / 2
    cell = size / 9
    places = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
    return [_text(x + col * cell + 1, y + row * cell + 7, value, 2.1)
            for (row, col), value in zip(places, MANDA[lang])]


# These original vector scenes stay within the panel rectangles. Captions are
# separate example slots, so all three languages share the same pictured beats.
STORY_SCENES = (
    '<rect x="52" y="18" width="27" height="65"/><circle cx="70" cy="50" r="2"/><circle cx="27" cy="42" r="7"/><path d="M27 49 L27 73 M16 59 L39 59 M27 73 L17 87 M27 73 L39 87"/>',
    '<rect x="12" y="15" width="58" height="68"/><path d="M12 38 H70 M12 61 H70 M30 16 V82 M50 16 V82"/><circle cx="80" cy="55" r="6"/><path d="M80 61 V80"/>',
    '<path d="M12 34 Q32 25 50 37 Q68 25 88 34 V76 Q68 68 50 79 Q32 68 12 76 Z M50 37 V79 M23 49 H42 M58 49 H77"/>',
    '<circle cx="30" cy="33" r="6"/><circle cx="70" cy="33" r="6"/><path d="M30 39 V68 M70 39 V68 M15 56 H85 M24 76 H76"/><path d="M38 16 Q50 6 63 16"/>',
    '<path d="M12 75 H88 M34 75 L47 47 L64 75 M47 47 L47 22"/><circle cx="47" cy="17" r="5"/>',
    '<rect x="18" y="32" width="28" height="39"/><rect x="52" y="23" width="28" height="48"/><path d="M17 76 H83 M25 41 H39 M59 33 H74"/>',
    '<circle cx="25" cy="35" r="6"/><circle cx="72" cy="35" r="6"/><path d="M25 41 V70 M72 41 V70 M18 75 H80 M38 52 H60"/>',
    '<rect x="22" y="22" width="56" height="52"/><path d="M30 34 H69 M30 47 H61 M30 60 H51"/><circle cx="72" cy="83" r="4"/>',
)

IDEA_SCENES = (
    '<rect x="23" y="12" width="54" height="75"/><path d="M31 33 H69 M31 46 H62 M31 59 H66"/>',
    '<circle cx="48" cy="49" r="18"/><path d="M66 29 Q86 49 66 69 M72 20 Q96 49 72 78"/>',
    '<path d="M14 76 L39 53 L60 61 L85 24 M14 76 L36 77 M85 24 L69 25"/><circle cx="39" cy="53" r="4"/>',
    '<rect x="18" y="50" width="64" height="23"/><path d="M23 50 V28 H76 V50 M26 73 V86 M74 73 V86"/>',
    '<path d="M18 78 Q37 19 57 54 Q68 69 83 22"/><circle cx="18" cy="78" r="5"/><circle cx="83" cy="22" r="5"/>',
    '<path d="M13 26 H61 V62 H39 L28 75 V62 H13 Z M46 40 H87 V75 H70 L61 87 V75"/>',
    '<rect x="17" y="22" width="30" height="53"/><rect x="53" y="22" width="30" height="53"/><path d="M22 33 H41 M58 33 H78 M22 46 H41 M58 46 H78"/>',
    '<rect x="15" y="21" width="70" height="55"/><path d="M15 63 H85 M33 76 V86 M67 76 V86 M24 35 H75"/>',
)

TEACHING_MARK_IDS = frozenset({
    "storyboard-6", "music-staff", "three-way-comparison", "three-columns",
    "fishbone", "mindmap-six", "mandala-9x9", "storyboard-three",
    "storyboard-four", "two-sketch-notes", "mixed-storyboard",
    "storyboard-eight-mixed", "crazy-eight", "seven-ideation-cards",
    "three-sketch-proposals", "main-sketch-side-notes", "detail-sketch",
    "ruled-sketch-top", "ruled-and-sketch", "perspective-guides",
    "blank", "grid-fine", "grid-standard", "grid-large", "engineering-grid",
    "dot-fine", "dot-standard", "dot-staggered", "dot-grid-split",
    "pixel-stitch-grid", "dot-and-blank", "hero-three-cards",
    "mosaic-cards", "hybrid-multi-zone", "column-dot-main",
    "quadrant", "cross-compare",
    "grid-hierarchical", "triangular-grid", "isometric-grid", "hex-grid",
    "rhombus-grid", "diagonal-guides", "radial-polar",
})


def _draw_in_rects(s: Scene, scenes: tuple[str, ...], *, card: bool = False):
    rects = [shape.values for shape in s.shapes if shape.kind == "rect"]
    marks = []
    for index, (x, y, w, h) in enumerate(rects[:len(scenes)]):
        inset = 4
        top = 20 if card else inset
        inner_h = max(6, h - top - inset)
        scale = min((w - 2 * inset) / 100, inner_h / 100)
        draw_x = x + (w - 100 * scale) / 2
        draw_y = y + top + (inner_h - 100 * scale) / 2
        marks.append(f'<g transform="translate({draw_x:.2f} {draw_y:.2f}) '
                     f'scale({scale:.5f})">'
                     f'{scenes[index]}</g>')
    return marks


ROUTE_SCENES = (
    '<circle cx="18" cy="70" r="5"/><path d="M23 70 H78 M68 63 L78 70 L68 77"/>',
    '<circle cx="50" cy="50" r="27"/><path d="M32 30 Q58 15 72 42 M72 42 L61 38 M72 42 L69 31"/>',
    '<path d="M18 76 L48 49 L78 24 M48 49 L80 75 M67 20 L78 24 L73 34 M70 68 L80 75 L67 78"/>',
)


def _selected_rect_scenes(s: Scene, indices: tuple[int, ...], scenes: tuple[str, ...]):
    rects = [shape.values for shape in s.shapes if shape.kind == "rect"]
    marks = []
    for index, drawing in zip(indices, scenes):
        x, y, w, h = rects[index]
        marks.append(f'<g transform="translate({x + 5:.2f} {y + 15:.2f}) '
                     f'scale({(w - 10) / 100:.5f} {(h - 19) / 100:.5f})">{drawing}</g>')
    return marks


VENUE_PLAN = '<path d="M12 12 H82 V82 H12 Z M12 47 H28 M28 47 V72 M28 72 H13"/><rect x="39" y="22" width="18" height="13"/><rect x="61" y="22" width="14" height="13"/><rect x="39" y="52" width="18" height="13"/><path d="M22 77 L42 77 M37 72 L42 77 L37 82"/>'
ENTRANCE_SIGN = '<rect x="20" y="28" width="65" height="36"/><path d="M31 46 H72 M61 37 L72 46 L61 55"/><path d="M52 64 V83"/>'
RAIN_COLLECTOR = '<path d="M14 20 L48 20 L53 38 L82 38 M70 38 L70 70 Q70 79 58 79 H38 Q28 79 28 70 V48"/><rect x="50" y="34" width="13" height="9"/><path d="M34 61 H65 M48 34 V22"/>'


def _sketch(s: Scene, kind: str):
    if kind == "ruled-sketch-top":
        x, y, w, h, drawing = s.left + 20, s.top + 25, s.width - 40, 45, RAIN_COLLECTOR
    elif kind == "ruled-and-sketch":
        x, y, w, h, drawing = s.left + 20, s.top + 129, s.width - 40, 47, RAIN_COLLECTOR
    elif kind == "main-sketch-side-notes":
        x, y, w, h, drawing = s.left + 12, s.top + 52, 62, 105, VENUE_PLAN
    else:  # detail-sketch, main drawing plus a genuinely enlarged entrance sign
        x, y, w, h, drawing = s.left + 10, s.top + 50, 57, 108, VENUE_PLAN
    parts = [f'<g transform="translate({x:.2f} {y:.2f}) scale({w/100:.5f} {h/100:.5f})">{drawing}</g>']
    if kind == "detail-sketch":
        parts += [f'<g transform="translate({s.right-34:.2f} {s.top+30:.2f}) scale(.25 .25)">{ENTRANCE_SIGN}</g>',
                  _circle(s.left + 24, s.top + 133, 5),
                  _line(s.left + 29, s.top + 130, s.right - 35, s.top + 46)]
    return parts


def _perspective(s: Scene):
    # A fictional display table: front, top and side planes converge toward
    # the sheet's two vanishing-point guides.
    x, y = (s.left + s.right) / 2, s.top + s.height * .46
    return [f'<path d="M{x-18:.2f} {y+28:.2f} L{x+14:.2f} {y+28:.2f} '
            f'L{x+24:.2f} {y+39:.2f} L{x-27:.2f} {y+39:.2f} Z '
            f'M{x-27:.2f} {y+39:.2f} V{y+73:.2f} L{x+24:.2f} {y+73:.2f} '
            f'V{y+39:.2f} M{x-18:.2f} {y+28:.2f} V{y+62:.2f} '
            f'M{x+14:.2f} {y+28:.2f} V{y+62:.2f}"/>']


def _grid_plan(s: Scene, kind: str):
    x, y = s.left + 26, s.top + 58
    if kind == "pixel-stitch-grid":
        # Four filled cells form a visible motif; these appear only in examples.
        return [f'<rect x="{x + dx:.2f}" y="{y + dy:.2f}" width="6" height="6" fill="#8A9CA5" stroke="none"/>'
                for dx, dy in ((0, 0), (6, 0), (0, 6), (6, 6))]
    return [_rect(x, y, 34, 24), _rect(x + 58, y + 32, 21, 18),
            _line(x + 34, y + 12, x + 58, y + 12),
            _line(x + 58, y + 12, x + 58, y + 32),
            _line(x + 51, y + 26, x + 58, y + 32),
            _line(x + 65, y + 26, x + 58, y + 32)]


def _dot_plan(s: Scene, kind: str):
    cx, cy = (s.left + s.right) / 2, s.top + 91
    if kind == "dot-grid-split":
        return [_circle(cx, s.top + 62, 6), _line(cx, s.top + 68, cx, s.top + 91),
                _line(cx, s.top + 82, cx - 15, s.top + 73),
                _line(cx, s.top + 82, cx + 15, s.top + 73),
                *[_rect(s.left + 18 + i * 32, s.top + 138, 17, 12) for i in range(3)]]
    return [_circle(cx, cy, 8), _circle(cx - 34, cy + 37, 8), _circle(cx + 34, cy + 37, 8),
            _line(cx - 6, cy + 7, cx - 28, cy + 30),
            _line(cx + 6, cy + 7, cx + 28, cy + 30),
            _line(cx - 26, cy + 37, cx + 26, cy + 37)]


def _hybrid_plan(s: Scene, kind: str):
    if kind == "dot-and-blank":
        return [_rect(s.left + 36, s.top + 145, 42, 26),
                _circle(s.left + 27, s.top + 163, 3),
                _line(s.left + 30, s.top + 163, s.left + 36, s.top + 163),
                _line(s.left + 78, s.top + 158, s.left + 98, s.top + 158)]
    if kind == "column-dot-main":
        return [_rect(s.left + 45, s.top + 72, 45, 26),
                _rect(s.left + 57, s.top + 119, 24, 18),
                _line(s.left + 64, s.top + 98, s.left + 64, s.top + 119)]
    if kind == "hybrid-multi-zone":
        return [_rect(s.left + 35, s.top + 71, 42, 22),
                _rect(s.left + 23, s.top + 99, 20, 12),
                _line(s.left + 43, s.top + 105, s.left + 70, s.top + 93)]
    # The large hero or mosaic card depicts a simple original rain collector.
    return [f'<g transform="translate({s.left + 20:.2f} {s.top + 31:.2f}) scale(.55 .48)">{RAIN_COLLECTOR}</g>']


QUADRANT_AXES = {
    "zh-TW": ("參與價值 ↑", "準備投入 →"),
    "en": ("Value ↑", "Preparation →"),
    "ja": ("参加価値 ↑", "準備の手間 →"),
}


def _quadrant_axes(s: Scene, lang: str):
    mid_y = (s.top + s.bottom) / 2
    vertical, horizontal = QUADRANT_AXES[lang]
    return [_text(s.left + 3, mid_y - 3, vertical, 2.4),
            _text((s.left + s.right) / 2 + 3, mid_y - 3, horizontal, 2.4)]


def _geometry_example(s: Scene, kind: str):
    x, y = s.left + 23, s.top + 79
    if kind in ("triangular-grid", "isometric-grid"):
        return [_line(x, y + 51, x + 40, y),
                _line(x + 40, y, x + 81, y + 51),
                _line(x, y + 51, x + 81, y + 51),
                _line(x + 40, y, x + 40, y + 51)]
    if kind == "hex-grid":
        return [_circle(x + 5, y + 20, 4), _circle(x + 47, y + 46, 4),
                _circle(x + 87, y + 15, 4),
                _line(x + 9, y + 22, x + 43, y + 44),
                _line(x + 51, y + 43, x + 83, y + 17)]
    if kind in ("rhombus-grid", "diagonal-guides"):
        return [_line(x, y + 48, x + 25, y + 17),
                _line(x + 25, y + 17, x + 56, y + 39),
                _line(x + 56, y + 39, x + 84, y + 8),
                _circle(x, y + 48, 3), _circle(x + 84, y + 8, 3)]
    if kind == "radial-polar":
        cx, cy = (s.left + s.right) / 2, (s.top + s.bottom) / 2
        return [_circle(cx, cy, 10), _circle(cx, cy - 57, 4),
                _circle(cx + 45, cy + 33, 4), _circle(cx - 43, cy + 34, 4),
                _line(cx, cy - 10, cx, cy - 53),
                _line(cx + 8, cy + 6, cx + 41, cy + 30),
                _line(cx - 8, cy + 6, cx - 39, cy + 30)]
    return _grid_plan(s, kind)


def example_marks(layout_id: str, scene: Scene, lang: str) -> list[str]:
    """Return semantic marks; no blank exporter calls this function."""
    if layout_id == "storyboard-6":
        marks = _storyboard(scene)
    elif layout_id == "music-staff":
        marks = _music(scene)
    elif layout_id == "three-way-comparison":
        marks = _three_way(scene, lang, True)
    elif layout_id == "three-columns":
        marks = _three_way(scene, lang, False)
    elif layout_id == "fishbone":
        marks = _fishbone(scene, lang)
    elif layout_id == "mindmap-six":
        marks = _mindmap(scene, lang)
    elif layout_id == "mandala-9x9":
        marks = _mandala(scene, lang)
    elif layout_id in ("storyboard-three", "storyboard-four", "two-sketch-notes",
                       "mixed-storyboard", "storyboard-eight-mixed"):
        marks = _draw_in_rects(scene, STORY_SCENES[:len(scene.slots)])
    elif layout_id in ("crazy-eight", "seven-ideation-cards"):
        marks = _draw_in_rects(scene, IDEA_SCENES[:len(scene.slots)], card=True)
    elif layout_id == "three-sketch-proposals":
        marks = _selected_rect_scenes(scene, (0, 2, 4), ROUTE_SCENES)
    elif layout_id in ("ruled-sketch-top", "ruled-and-sketch",
                       "main-sketch-side-notes", "detail-sketch"):
        marks = _sketch(scene, layout_id)
    elif layout_id == "perspective-guides":
        marks = _perspective(scene)
    elif layout_id == "blank":
        marks = [_line(scene.left + 24, scene.top + 111, scene.left + 24, scene.top + 143),
                 _line(scene.left + 24, scene.top + 120, scene.left + 8, scene.top + 111),
                 _line(scene.left + 24, scene.top + 127, scene.left + 39, scene.top + 116),
                 _rect(scene.left + 15, scene.top + 143, 18, 15)]
    elif layout_id in ("grid-fine", "grid-standard", "grid-large", "engineering-grid", "pixel-stitch-grid"):
        marks = _grid_plan(scene, layout_id)
    elif layout_id in ("dot-fine", "dot-standard", "dot-staggered", "dot-grid-split"):
        marks = _dot_plan(scene, layout_id)
    elif layout_id in ("dot-and-blank", "hero-three-cards", "mosaic-cards",
                       "hybrid-multi-zone", "column-dot-main"):
        marks = _hybrid_plan(scene, layout_id)
    elif layout_id in ("quadrant", "cross-compare"):
        marks = _quadrant_axes(scene, lang)
    elif layout_id in ("grid-hierarchical", "triangular-grid", "isometric-grid",
                       "hex-grid", "rhombus-grid", "diagonal-guides", "radial-polar"):
        marks = _geometry_example(scene, layout_id)
    else:
        return []
    return ['<g data-example="teaching-marks" fill="none" stroke="#746F68" stroke-width="0.58" stroke-linecap="round" stroke-linejoin="round">', *marks, '</g>']

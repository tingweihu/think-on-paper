from __future__ import annotations

import html
import struct
from pathlib import Path

from .geometry import Scene
from .examples import example_marks

PT = 72 / 25.4
PDF_TITLE_X_MM = 14.0
PDF_TITLE_BASELINE_MM = 8.5
PDF_TITLE_SIZE_PT = 8.0


def _color(hex_color: str) -> tuple[float, float, float]:
    return tuple(int(hex_color[i:i + 2], 16) / 255 for i in (1, 3, 5))


def svg(scene: Scene, profile: dict) -> str:
    out = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{scene.page_w}mm" height="{scene.page_h}mm" viewBox="0 0 {scene.page_w} {scene.page_h}">',
    ]
    for s in scene.shapes:
        color = profile["ink"][s.layer]
        width = profile["stroke_mm"][s.layer]
        style = f'fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"'
        v = s.values
        if s.kind == "line":
            out.append(f'<line x1="{v[0]:.3f}" y1="{v[1]:.3f}" x2="{v[2]:.3f}" y2="{v[3]:.3f}" {style}/>')
        elif s.kind == "rect":
            out.append(f'<rect x="{v[0]:.3f}" y="{v[1]:.3f}" width="{v[2]:.3f}" height="{v[3]:.3f}" {style}/>')
        elif s.kind == "circle":
            out.append(f'<circle cx="{v[0]:.3f}" cy="{v[1]:.3f}" r="{v[2]:.3f}" {style}/>')
        elif s.kind == "dot":
            out.append(f'<circle cx="{v[0]:.3f}" cy="{v[1]:.3f}" r="{v[2]:.3f}" fill="{color}" stroke="none"/>')
        else:
            points = " ".join(f"{v[i]:.3f},{v[i + 1]:.3f}" for i in range(0, len(v), 2))
            tag = s.kind
            out.append(f'<{tag} points="{points}" {style}/>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


def _pdf_content(scene: Scene, profile: dict, title: str | None = None) -> bytes:
    out = ["1 J 1 j"]
    if title is not None:
        if not title or any(ord(char) < 32 for char in title):
            raise ValueError("A titled PDF needs one printable English name")
        title.encode("cp1252")  # Standard Helvetica with WinAnsiEncoding.
        if PDF_TITLE_BASELINE_MM >= scene.top:
            raise ValueError("PDF title overlaps the geometry's safe top margin")
        escaped = title.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
        gray = _color("#655F57")
        out.append(
            f"{gray[0]:.5f} {gray[1]:.5f} {gray[2]:.5f} rg "
            f"BT /F1 {PDF_TITLE_SIZE_PT:.2f} Tf "
            f"{PDF_TITLE_X_MM*PT:.4f} {(scene.page_h-PDF_TITLE_BASELINE_MM)*PT:.4f} Td "
            f"({escaped}) Tj ET"
        )
    for s in scene.shapes:
        color = _color(profile["ink"][s.layer])
        width = profile["stroke_mm"][s.layer] * PT
        out.append(f"{color[0]:.5f} {color[1]:.5f} {color[2]:.5f} RG {width:.5f} w")
        v = s.values
        if s.kind == "line":
            out.append(f"{v[0]*PT:.4f} {(scene.page_h-v[1])*PT:.4f} m {v[2]*PT:.4f} {(scene.page_h-v[3])*PT:.4f} l S")
        elif s.kind == "rect":
            out.append(f"{v[0]*PT:.4f} {(scene.page_h-v[1]-v[3])*PT:.4f} {v[2]*PT:.4f} {v[3]*PT:.4f} re S")
        elif s.kind in ("circle", "dot"):
            x, y, r = v
            k = 0.5522847498 * r
            def p(xx, yy): return f"{xx*PT:.4f} {(scene.page_h-yy)*PT:.4f}"
            out.append(" ".join([
                f"{p(x+r,y)} m",
                f"{p(x+r,y+k)} {p(x+k,y+r)} {p(x,y+r)} c",
                f"{p(x-k,y+r)} {p(x-r,y+k)} {p(x-r,y)} c",
                f"{p(x-r,y-k)} {p(x-k,y-r)} {p(x,y-r)} c",
                f"{p(x+k,y-r)} {p(x+r,y-k)} {p(x+r,y)} c {'f' if s.kind == 'dot' else 'S'}",
            ]))
        else:
            pts = list(zip(v[::2], v[1::2]))
            seq = [f"{pts[0][0]*PT:.4f} {(scene.page_h-pts[0][1])*PT:.4f} m"]
            seq.extend(f"{x*PT:.4f} {(scene.page_h-y)*PT:.4f} l" for x, y in pts[1:])
            seq.append("h S" if s.kind == "polygon" else "S")
            out.append(" ".join(seq))
    return ("\n".join(out) + "\n").encode("cp1252")


def pdf(scene: Scene, profile: dict, title: str | None = None) -> bytes:
    content = _pdf_content(scene, profile, title)
    w, h = scene.page_w * PT, scene.page_h * PT
    resources = "<< /Font << /F1 5 0 R >> >>" if title is not None else "<< >>"
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {w:.4f} {h:.4f}] /Resources {resources} /Contents 4 0 R >>".encode(),
        f"<< /Length {len(content)} >>\nstream\n".encode() + content + b"endstream",
    ]
    if title is not None:
        objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
    buf = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for i, obj in enumerate(objects, 1):
        offsets.append(len(buf))
        buf.extend(f"{i} 0 obj\n".encode() + obj + b"\nendobj\n")
    xref = len(buf)
    buf.extend(f"xref\n0 {len(objects)+1}\n0000000000 65535 f \n".encode())
    for off in offsets[1:]:
        buf.extend(f"{off:010d} 00000 n \n".encode())
    buf.extend(f"trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode())
    return bytes(buf)


def example_svg(scene: Scene, profile: dict, labels: list[str], lang: str, layout_id: str = "") -> str:
    if len(labels) != len(scene.slots):
        raise ValueError(f"Example has {len(labels)} labels but layout has {len(scene.slots)} slots")
    source = svg(scene, profile)
    overlay = example_marks(layout_id, scene, lang)
    overlay.append(f'<g xml:lang="{html.escape(lang)}" fill="#524E48" font-family="Arial, sans-serif" font-size="3.0">')
    for label, (x, y, width) in zip(labels, scene.slots):
        # Keep authored labels short; text remains editable in the SVG source.
        max_chars = max(5, int(width / (3.0 if lang != "en" else 1.75)))
        words = list(label) if lang != "en" else label.split(" ")
        lines, line = [], ""
        for word in words:
            if lang == "en" and len(word) > max_chars:
                if line:
                    lines.append(line)
                    line = ""
                while len(word) > max_chars:
                    lines.append(word[:max_chars - 1] + "-")
                    word = word[max_chars - 1:]
            candidate = line + ("" if lang != "en" or not line else " ") + word
            if len(candidate) > max_chars and line:
                lines.append(line)
                line = word
            else:
                line = candidate
        if line:
            lines.append(line)
        if len(lines) > 3:
            raise ValueError(f"Example label needs more than three lines: {layout_id}/{lang}: {label}")
        if layout_id == "music-staff":
            continue  # Notes and rhythm, not letter names, are the teaching example.
        for i, row in enumerate(lines):
            overlay.append(f'<text x="{x:.3f}" y="{y + i*4.3:.3f}">{html.escape(row)}</text>')
    overlay.append("</g>")
    return source.replace("</svg>", "\n".join(overlay) + "\n</svg>")

"""Stable review identity, independent of PNG compression and metadata."""

import hashlib
import json
from pathlib import Path

from PIL import Image


def geometry_digest(scene) -> str:
    shapes = [[s.kind, [round(v, 4) for v in s.values], s.layer] for s in scene.shapes]
    return hashlib.sha256(json.dumps(shapes, separators=(",", ":")).encode()).hexdigest()


def appearance_digest(profile: dict) -> str:
    keys = ("page_mm", "stroke_mm", "ink", "preview_paper", "dot_diameter_mm", "line_cap", "line_join")
    data = {key: profile[key] for key in keys}
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def pixel_digest(path: Path) -> str:
    with Image.open(path) as image:
        rgb = image.convert("RGB")
        header = f"RGB:{rgb.width}:{rgb.height}:".encode()
        return hashlib.sha256(header + rgb.tobytes()).hexdigest()


def review_valid(root: Path, note: dict, geometry: str, profile: dict) -> bool:
    evidence = (root / note.get("evidence", "")).resolve()
    return bool(note.get("date") and note.get("finding")
                and note.get("geometry_sha256") == geometry
                and note.get("appearance_sha256") == appearance_digest(profile)
                and root in evidence.parents and evidence.is_file()
                and note.get("evidence_pixel_sha256") == pixel_digest(evidence))

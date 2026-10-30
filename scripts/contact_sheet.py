from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]

import sys
sys.path.insert(0, str(ROOT / "src"))
from noteformats.safety import assert_safe_workspace, safe_project_path
assert_safe_workspace(ROOT)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="*", help="Layout IDs; default is every generated preview")
    parser.add_argument("--output", default="reports/contact-sheet.png")
    args = parser.parse_args()
    ids = args.ids or [p.parent.parent.name for p in sorted((ROOT / "templates").glob("*/previews/a5-draft.png"))]
    images = []
    for layout_id in ids:
        if not layout_id.replace("-", "").isalnum() or layout_id.lower() != layout_id:
            raise ValueError(f"Unsafe layout ID: {layout_id}")
        path = safe_project_path(ROOT, Path("templates") / layout_id / "previews" / "a5-draft.png")
        if not path.is_file():
            raise FileNotFoundError(path)
        with Image.open(path) as im:
            thumb = im.convert("RGB")
            thumb.thumbnail((260, 370))
            images.append((layout_id, thumb.copy()))
    cols = min(4, max(1, len(images)))
    rows = (len(images) + cols - 1) // cols
    cell_w, cell_h = 286, 415
    sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), "#EAE8E3")
    draw = ImageDraw.Draw(sheet)
    for n, (layout_id, im) in enumerate(images):
        x = (n % cols) * cell_w + (cell_w - im.width) // 2
        y = (n // cols) * cell_h + 14
        sheet.paste(im, (x, y))
        draw.rectangle((x, y, x + im.width - 1, y + im.height - 1), outline="#CBC5B9")
        draw.text(((n % cols) * cell_w + 12, (n // cols) * cell_h + 387), layout_id, fill="#423F3A")
    dest = safe_project_path(ROOT, args.output)
    dest.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(dest, optimize=True)
    print(dest.relative_to(ROOT))


if __name__ == "__main__":
    main()

# Customize and rebuild

[Home](../../README.en.md) · [繁體中文](../zh-TW/customize.md) · [日本語](../ja/customize.md)

Paper size, margins, strokes, ink, and preview paper color live in [`profiles/a5-draft.json`](../../profiles/a5-draft.json). Shared primitives live in [`src/noteformats/geometry.py`](../../src/noteformats/geometry.py), base builders in `src/noteformats/layouts/`, and parameter variants in `src/noteformats/variants.py`. Example text lives in `content/` and `src/noteformats/variant_content.py`; it never enters the blank sheet.

Building requires Python 3.12, Pillow and pypdf from [`requirements.txt`](../../requirements.txt), and Poppler `pdftoppm` on PATH. This verification used Python 3.12.10, Pillow 12.1.1, pypdf 6.7.5, and Poppler 26.07.0. Once dependencies are available locally, generation and QA work offline.

From the project root run:

```powershell
python scripts/build.py --ids quadrant
python -B scripts/generate_docs.py
python scripts/qa.py
```

The build also writes `titled.pdf` with the English format name at top left. The original `blank.pdf` and SVG remain wordless; the PNG still comes from the blank PDF. QA checks the name and PDF page for every format.

The first command regenerates the blank SVG and PDF, the PDF-rendered PNG, and the language examples. The final command checks dimensions, wordlessness, content, and paths. Omit `--ids` to build every implemented format. Treat `templates/*/exports/` as reproducible output.

## Windows, macOS and Linux

Use a local checkout in any directory and run commands from its root. The generator discovers the root from its own script location. Python 3.12, the pinned Python packages, and Poppler's `pdftoppm` must be available locally.

- Windows PowerShell: `python -B scripts/build.py`, then `python -B scripts/generate_docs.py` and `python -B scripts/qa.py`.
- macOS or Linux shell: `python3 -B scripts/build.py`, then `python3 -B scripts/generate_docs.py` and `python3 -B scripts/qa.py`.

The generator rejects linked project entries, traversal paths, and output paths outside its checkout.

[Build and verify](../BUILD-AND-VERIFY.md)

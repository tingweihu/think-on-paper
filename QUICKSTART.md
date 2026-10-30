# Quick start｜快速開始｜はじめに

1. Open the [繁中目錄](docs/zh-TW/catalog.md), [English catalog](docs/en/catalog.md), or [日本語一覧](docs/ja/catalog.md). The three homepages show all 144 formats with previews, uses, and worked examples.
2. Download `blank.pdf` for a wordless A5 page, `titled.pdf` for the English name at the top left, or `blank.svg` for vector editing. PNG is a preview rendered from `blank.pdf`.
3. For printing, choose **A5, 148 × 210 mm, actual size / 100%**. The warm-yellow preview color is not printed as a full-page fill. Physical print results depend on the printer and paper.
4. To rebuild locally, provide Python 3.12, the packages in [`requirements.txt`](requirements.txt), and Poppler `pdftoppm`. From the repository root run `python -B scripts/build.py` then `python -B scripts/generate_docs.py` and `python -B scripts/qa.py`. See each language's `customize.md` for details.

Original project content is [MIT licensed](LICENSE). For provenance and third-party boundaries, see [Sources and rights](docs/SOURCES-AND-RIGHTS.md).

Build and verification behavior: [Build and verify](docs/BUILD-AND-VERIFY.md).

# Build and verify

From the repository root, with Python 3.12, the versions in `requirements.txt`, and Poppler `pdftoppm` available locally:

```shell
python -B scripts/build.py
python -B scripts/generate_docs.py
python -B scripts/qa.py
python -B -m unittest discover -s tests
python -B scripts/release_check.py
```

Use `python3` when that is the Python command on your system. Each audit script also runs independently on the shipped files and creates its local output directory. `release_check.py` checks public files directly; it does not depend on a previous QA report and does not replace the full QA command.

If an existing Poppler installation is not on PATH, both build and QA accept `--pdftoppm "<full-path-to-pdftoppm>"`. They check the renderer before writing outputs or reports. A missing renderer exits with code 2 and one setup error; it does not mark every format as broken or replace the last QA reports. No automatic installation or global PATH change is performed.

`qa.py` writes local reports only, including when validation fails. Public README and indexes change only through `generate_docs.py`, which preserves unchanged files. The full gallery is generated from the same content as each template page; edits belong in `content/` or the variant content module.

Recorded visual reviews bind geometry and appearance settings to decoded evidence pixels. PNG compression and metadata do not change a review's validity. Preview pixels are still checked against a fresh rendering of the corresponding PDF in the current environment. An actual geometry or appearance change requires a renewed review; `seal_reviews.py` refuses to approve it automatically.

The default ink remains light. Every ID also has darker blank SVG/PDF and an English-titled PDF under `exports/a5-contrast/`, with identical geometry and no full-page fill. The three ink colors have white-background contrast ratios of approximately 4.74, 7.00 and 12.63 to one. These values describe digital color contrast, not a printer certification.

Python package versions are exact pins, not a complete dependency hash lock. Poppler is an external renderer: its version is reported in build evidence and the Linux CI configuration requires upstream 24.02.0. Raster encoding and antialiasing may differ between versions; stable source vectors and review identity do not rely on PNG file bytes. The prepared CI must run on the hosting service before its result can be claimed.

The test suite makes an in-project public-file-only copy without local reports, runs commands in arbitrary order, re-encodes PNGs, and corrupts one output to verify that QA fails while public documentation stays intact.

Variant-specific usage scenarios live in `content/usage-scenarios.json`; named-method step corrections live in `content/method-guidance.json`; format-specific limitations live in `content/format-limitations.json`. The content loader applies these records before generating each language page. QA and the documentation audit reject identical scenario sets or limitation text across IDs, repeated scenarios within a page, and repeated sentences in descriptions. These checks catch copying errors; matching content to its method still requires reading it.

Generated worked-example entries are stored as a list and displayed as a numbered Markdown list, with one item per example label position. Commas inside an entry stay inside that item. QA checks that the list and its presentation match the labels used in the example SVG. Compact references within instructions also number and quote each entry.

Public text uses LF through `.gitattributes`, and the release checker reports CRLF regressions. CI has read-only repository permissions and rejects untracked public files after rebuilding. Tracked PNG encoding differences are allowed only alongside the PDF-to-pixel checks; all other tracked changes fail the rebuild check. Action version tags still need to be resolved to verified commit SHAs before claiming immutable action dependencies.

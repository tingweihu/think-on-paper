# Narrow right column

`two-right-narrow` · `columns` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [Back to catalog](../../docs/en/catalog.md)

![Narrow right column](previews/a5-draft.png)

Put short references and open questions in the narrow right column, leaving the left for continuous notes or sketches.

## When to use it

**Geometry relationship:** `parameter` · [two-left-narrow](../two-left-narrow/README.en.md)

- Write reading notes on the left and reserve the narrow right column for page numbers and terms to check.
- Sketch a venue on the left while collecting dimension questions and check marks in the right rail.

## How to use it

1. Use the large left area for notes or sketches and the narrow right rail for page numbers, source codes or short questions.
2. Match related entries with the same mark and keep long sentences out of the right rail.
3. Review the right-hand questions and mark those still unresolved.

## What the page helps you see

Parallel notes whose agreements, differences, and unanswered points can be checked.


## Worked example

Entries in example-position order; each number identifies one entry:

1. Venue
2. Entrance near shelves; seats by window.

![Narrow right column worked example](examples/en.svg)

[SVG](examples/en.svg)

## When not to use it

For a bottom summary and self-testing by covering the main text, choose a Cornell layout. Small cells hold short phrases rather than long paragraphs.

## Downloads

- [Wordless SVG](exports/a5-draft/blank.svg)
- [Wordless PDF](exports/a5-draft/blank.pdf)
- [PDF with English name at top left](exports/a5-draft/titled.pdf)
- [Darker-ink wordless PDF](exports/a5-contrast/blank.pdf)
- [Darker-ink SVG](exports/a5-contrast/blank.svg)

The English name appears only on the titled PDF; the wordless version remains available for free writing.

Page size: A5 (148 × 210 mm); profile: `a5-draft`.

## Provenance and status

Generic geometry · Detailed source record: [manifest.json](manifest.json)  
[MIT license scope](../../LICENSE-SCOPE.md)

[Trilingual glossary](../../docs/en/glossary.md)

## Modify and rebuild

Edit geometry in `src/noteformats/variants.py` or text in `src/noteformats/variant_content.py`, then run from the project root:

`python scripts/build.py --ids two-right-narrow`

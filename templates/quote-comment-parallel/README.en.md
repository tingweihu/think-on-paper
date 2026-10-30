# Quotation and comment

`quote-comment-parallel` · `research` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [Back to catalog](../../docs/en/catalog.md)

![Quotation and comment](previews/a5-draft.png)

Place a fictional quotation beside a separate checkable comment.

## When to use it

**Geometry relationship:** `equivalent` · [two-equal-columns](../two-equal-columns/README.en.md)

- Keep an article's exact passage in one column and your comments or questions in the other.
- Compare fictional interview excerpts with analysis notes without mixing interpretation into quotations.

## How to use it

1. Place a fictional quotation beside a separate checkable comment.
2. Keep corresponding items at similar heights, adding arrows if useful.
3. Look for items present on only one side and note which source needs checking.

## What the page helps you see

Sources, quotations, claims, and open checks kept distinct.


## Worked example

Entries in example-position order; each number identifies one entry:

1. Quote: 'Open Saturday'
2. Note: verify date and source

![Quotation and comment worked example](examples/en.svg)

[SVG](examples/en.svg)

## When not to use it

A comment beside a quotation does not show the author agrees with your interpretation; distinguish quotation from paraphrase and avoid stripping multi-paragraph arguments into isolated lines.

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

`python scripts/build.py --ids quote-comment-parallel`

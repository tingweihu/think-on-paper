# Quotation with side notes

`quote-side-notes` · `research` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [Back to catalog](../../docs/en/catalog.md)

![Quotation with side notes](previews/a5-draft.png)

Keep a short quotation in the wide column and source questions at its side.

## When to use it

**Geometry relationship:** `equivalent` · [two-left-narrow](../two-left-narrow/README.en.md)

- Copy a passage into the large column and put its page reference and vocabulary notes in the narrow left rail.
- Keep a fictional poster's wording intact while noting date or phrasing questions beside it.

## How to use it

1. Keep a short quotation in the wide column and source questions at its side.
2. Record the main material on the right at roughly the same height as its cue.
3. Review using the rail and check that the main text still has enough context.

## What the page helps you see

Sources, quotations, claims, and open checks kept distinct.


## Worked example

Entries in example-position order; each number identifies one entry:

1. Check date
2. Fictional poster: 'Open Saturday afternoon.'

![Quotation with side notes worked example](examples/en.svg)

[SVG](examples/en.svg)

## When not to use it

The side rail holds brief annotations rather than full context and provenance; check the surrounding passage so a short excerpt does not change the original meaning.

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

`python scripts/build.py --ids quote-side-notes`

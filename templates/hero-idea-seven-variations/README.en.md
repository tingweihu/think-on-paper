# Hero idea with seven variations

`hero-idea-seven-variations` · `ideation` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [Back to catalog](../../docs/en/catalog.md)

![Hero idea with seven variations](previews/a5-draft.png)

Keep one main proposal in the center and test seven variations around it. Geometry change: outer variation cards: 7.

## When to use it

**Geometry relationship:** `parameter` · [center-eight-boxes](../center-eight-boxes/README.en.md)

- Draw a core poster idea in the center and try one layout change on each of seven outer cards.
- Start from one service proposal and explore seven material, process or interaction variations.

## How to use it

1. Put the core proposal in the center and one modification on each outer card.
2. Use the worked example to place entries in region order: 1: "Venue"; 2: "Works"; 3: "Volunteers"; 4: "Tour"; 5: "Exhibition"; 6: "Access"; 7: "Materials"; 8: "Schedule"
3. Review the regions, mark open questions and choose a next step.

## What the page helps you see

Multiple proposals with a basis for the next selection step.


## Worked example

Entries in example-position order; each number identifies one entry:

1. Venue
2. Works
3. Volunteers
4. Tour
5. Exhibition
6. Access
7. Materials
8. Schedule

![Hero idea with seven variations worked example](examples/en.svg)

[SVG](examples/en.svg)

## When not to use it

The cards have no built-in sequence; position alone should not imply dependencies. Small cells hold short phrases rather than long paragraphs.

## Downloads

- [Wordless SVG](exports/a5-draft/blank.svg)
- [Wordless PDF](exports/a5-draft/blank.pdf)
- [PDF with English name at top left](exports/a5-draft/titled.pdf)
- [Darker-ink wordless PDF](exports/a5-contrast/blank.pdf)
- [Darker-ink SVG](exports/a5-contrast/blank.svg)

The English name appears only on the titled PDF; the wordless version remains available for free writing.

Page size: A5 (148 × 210 mm); profile: `a5-draft`.

## Provenance and status

Original layout · Detailed source record: [manifest.json](manifest.json)  
[MIT license scope](../../LICENSE-SCOPE.md)

[Trilingual glossary](../../docs/en/glossary.md)

## Modify and rebuild

Edit geometry in `src/noteformats/variants.py` or text in `src/noteformats/variant_content.py`, then run from the project root:

`python scripts/build.py --ids hero-idea-seven-variations`

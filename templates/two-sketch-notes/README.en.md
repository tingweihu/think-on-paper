# Two sketch notes

`two-sketch-notes` · `storyboard` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [Back to catalog](../../docs/en/catalog.md)

![Two sketch notes](previews/a5-draft.png)

Show successive changes in one event, with a short action cue for every frame. Geometry change: storyboard frames: 2.

## When to use it

**Geometry relationship:** `parameter` · [storyboard-6](../storyboard-6/README.en.md)

- Draw an object before and after a revision in two sketch areas and note why it changed.
- Use two pictures to compare how the same entrance can be recognized by day and by night.

## How to use it

1. Divide the event into the number of frames on this page and draw a visible change in each.
2. Use the worked example to place entries in region order: 1: "Entrance sketch"; 2: "Interior sketch"
3. Review the regions, mark open questions and choose a next step.

## What the page helps you see

A visual sequence showing transitions and missing shots.


## Worked example

Entries in example-position order; each number identifies one entry:

1. Entrance sketch
2. Interior sketch

![Two sketch notes worked example](examples/en.svg)

[SVG](examples/en.svg)

## When not to use it

Two pictures support a paired comparison but cannot by themselves explain three or more successive states; add a flow or more frames to show the transition process.

## Downloads

- [Wordless SVG](exports/a5-draft/blank.svg)
- [Wordless PDF](exports/a5-draft/blank.pdf)
- [PDF with English name at top left](exports/a5-draft/titled.pdf)
- [Darker-ink wordless PDF](exports/a5-contrast/blank.pdf)
- [Darker-ink SVG](exports/a5-contrast/blank.svg)

The English name appears only on the titled PDF; the wordless version remains available for free writing.

Page size: A5 (148 × 210 mm); profile: `a5-draft`.

## Provenance and status

Adaptation of a traditional format · Detailed source record: [manifest.json](manifest.json)  
[MIT license scope](../../LICENSE-SCOPE.md)

[Trilingual glossary](../../docs/en/glossary.md)

## Modify and rebuild

Edit geometry in `src/noteformats/variants.py` or text in `src/noteformats/variant_content.py`, then run from the project root:

`python scripts/build.py --ids two-sketch-notes`

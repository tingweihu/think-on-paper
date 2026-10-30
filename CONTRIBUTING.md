# Contributing

Original project code, documentation, examples, and artwork are under the [MIT License](LICENSE). Keep the copyright and license notice when redistributing copies or substantial portions.

1. Check `catalog-144.csv`, the trilingual catalog, and existing template manifests before proposing a new ID. Explain its writing behavior and geometry difference; spacing, mirror, and count changes normally belong to a variant family.
2. Submit only code or content you have the right to provide under MIT. Identify the author and source of each contribution. Do not include another person's private notes, commercial template, unlicensed image, font, or trademark.
3. Add a builder or variant definition, three-language purpose, scenarios, steps, a concrete worked example, limits, and a source note. Keep `blank.svg` and `blank.pdf` wordless. Check that the trilingual homepage displays the matching example image and scenario for the new ID.
4. Rebuild locally with `python -B scripts/build.py`, then run `python -B scripts/qa.py`. Include the exact commands and outcomes with the proposed change. For a print issue, include A5 paper, printer scaling, pen, and measured dimensions; do not upload private notes.
5. Translation proposals must preserve meaning, limits, and example structure. State whether a native-speaking reviewer checked them. A digital preview may disclose that such review has not occurred; do not claim it has passed.

See [繁體中文](docs/zh-TW/contribute.md), [English](docs/en/contribute.md), and [日本語](docs/ja/contribute.md). External contributions still require a source and rights check before inclusion.

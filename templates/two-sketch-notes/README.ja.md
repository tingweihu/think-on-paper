# 二枚の下書きノート

`two-sketch-notes` · `storyboard` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![二枚の下書きノート](previews/a5-draft.png)

一つの出来事の変化を連続したコマに描き、各コマに短い動作を添えます。 図形の変更： 絵コンテのコマ数: 2.

## 向いている場面

**図形の対応:** `parameter` · [storyboard-6](../storyboard-6/README.ja.md)

- 物の修正前と修正後を二つの描画欄に記し、変更理由を添えるとき。
- 同じ入口の昼と夜の見つけ方を二枚の図で比べるとき。

## 使い方

1. このページのコマ数に合わせて場面を分け、各コマに見える変化を描きます。
2. 記入例を参考に、領域の順で記します：1「入口の図」；2「内部の図」
3. 各領域を読み返し、未確認の点と次の行動を記します。

## 記入後に見えること

連続した場面から変化や足りないカットが見えます。


## 記入例

図の記入位置の順に示します。番号一つが一つの記入例です：

1. 入口の図
2. 内部の図

![二枚の下書きノート 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

二枚の図は一対の比較向けで、三つ以上の連続する状態をそれだけでは説明できません。変化の過程には流れ図や追加のコマを使います。

## ダウンロード

- [文字なしSVG](exports/a5-draft/blank.svg)
- [文字なしPDF](exports/a5-draft/blank.pdf)
- [左上に英語名があるPDF](exports/a5-draft/titled.pdf)
- [濃い線の文字なしPDF](exports/a5-contrast/blank.pdf)
- [濃い線のSVG](exports/a5-contrast/blank.svg)

英語名は表題付きPDFだけに印刷され、文字なし版は自由な記入に使えます。

用紙サイズ：A5（148 × 210 mm）。設定ファイル：`a5-draft`。

## 由来と状態

伝統的な形式の応用 · 詳しい由来の記録： [manifest.json](manifest.json)  
[MITライセンスの範囲](../../LICENSE-SCOPE.md)

[三言語の用語集](../../docs/ja/glossary.md)

## 変更と再生成

図形は `src/noteformats/variants.py`、文章は `src/noteformats/variant_content.py` を変更し、プロジェクトのルートで実行します：

`python scripts/build.py --ids two-sketch-notes`

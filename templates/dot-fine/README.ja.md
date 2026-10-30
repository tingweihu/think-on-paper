# 細かいドット方眼

`dot-fine` · `grid-dot` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![細かいドット方眼](previews/a5-draft.png)

薄い点で位置をそろえながら、方眼より自由な書き心地を残します。 図形の変更： ドットの間隔: 3.5 mm.

## 向いている場面

**図形の対応:** `parameter` · [dot-standard](../dot-standard/README.ja.md)

- 細かい点で小さなアイコンをそろえ、曲線は自由に描きたいとき。
- 短い記録と小さな関係図を同じページに置き、点で間隔を整えるとき。

## 使い方

1. 点は位置の目安として使い、すべてを埋めようとしません。
2. 主題を書き、必要な点だけを結んで枠や線を作ります。
3. 描いた構造が文章を分かりやすくしたか見直します。

## 記入後に見えること

方眼や点に沿って物、数、位置をそろえられます。


## 記入例

架空の地域イベントの会場、材料、担当者を三つのそろった区画で示しています。 架空の短い記入で各領域の使い方を示します。実測データや完全な調査結果ではありません。

![細かいドット方眼 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

明確なマス目や連続した書字の基準線が必要な場合、点だけでは弱すぎます。 小さなマスは短い語句向けで、長い文章には向きません。

## ダウンロード

- [文字なしSVG](exports/a5-draft/blank.svg)
- [文字なしPDF](exports/a5-draft/blank.pdf)
- [左上に英語名があるPDF](exports/a5-draft/titled.pdf)
- [濃い線の文字なしPDF](exports/a5-contrast/blank.pdf)
- [濃い線のSVG](exports/a5-contrast/blank.svg)

英語名は表題付きPDFだけに印刷され、文字なし版は自由な記入に使えます。

用紙サイズ：A5（148 × 210 mm）。設定ファイル：`a5-draft`。

## 由来と状態

伝統的な練習紙の応用 · 詳しい由来の記録： [manifest.json](manifest.json)  
[MITライセンスの範囲](../../LICENSE-SCOPE.md)

[三言語の用語集](../../docs/ja/glossary.md)

## 変更と再生成

図形は `src/noteformats/variants.py`、文章は `src/noteformats/variant_content.py` を変更し、プロジェクトのルートで実行します：

`python scripts/build.py --ids dot-fine`

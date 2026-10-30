# 田字格の漢字練習紙

`hanzi-tian` · `special-paper` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![田字格の漢字練習紙](previews/a5-draft.png)

縦横の中心線で、一字の左右と上下のバランスを見ます。

## 向いている場面

- 漢字一字の重心や部品の位置を練習するとき。
- 同じ字を繰り返し、余白の違いを比べるとき。

## 使い方

1. 一字を選び、最初の枠で中心を意識します。
2. 十字を基準に左右・上下の部分を見ながら書きます。
3. 各枠の余白と線の位置を見直し、一つ改善点を選びます。

## 記入後に見えること

専用の罫線に沿った記譜、文字、下書きを確認できます。


## 記入例

最初の三枠に編集可能な『永』を繰り返し、中心の位置を比較します。残りは空白です。

![田字格の漢字練習紙 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

十字は空間の補助で、字体の規範や筆順の教材ではありません。A5の一枠は約21 mmで長文には向きません。

## ダウンロード

- [文字なしSVG](exports/a5-draft/blank.svg)
- [文字なしPDF](exports/a5-draft/blank.pdf)
- [左上に英語名があるPDF](exports/a5-draft/titled.pdf)
- [濃い線の文字なしPDF](exports/a5-contrast/blank.pdf)
- [濃い線のSVG](exports/a5-contrast/blank.svg)

英語名は表題付きPDFだけに印刷され、文字なし版は自由な記入に使えます。

用紙サイズ：A5（148 × 210 mm）。設定ファイル：`a5-draft`。

## 由来と状態

一般的な幾何構造 · 詳しい由来の記録： [manifest.json](manifest.json)  
[MITライセンスの範囲](../../LICENSE-SCOPE.md)

[三言語の用語集](../../docs/ja/glossary.md)

## 変更と再生成

`profiles/a5-draft.json` または `src/noteformats/layouts/` の描画関数を変更し、プロジェクトのルートで実行します：

`python scripts/build.py --ids hanzi-tian`

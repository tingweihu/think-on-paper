# 米字格の漢字練習紙

`hanzi-mi` · `special-paper` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![米字格の漢字練習紙](previews/a5-draft.png)

十字と対角線で、斜めの画と字形の重心を見ます。

## 向いている場面

- 左右へ払う画のある字を練習するとき。
- 同じ字の四隅の余白を比べるとき。

## 使い方

1. 最初の枠で十字の中心を見つけます。
2. 斜線を目安にし、画を必ず重ねる線とは考えません。
3. 字を繰り返し、重心と四隅の余白を比べます。

## 記入後に見えること

専用の罫線に沿った記譜、文字、下書きを確認できます。


## 記入例

最初の三枠に編集可能な『大』を繰り返し、左右の払い方を比べます。

![米字格の漢字練習紙 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

対角線は画の固定角度ではありません。補助線が多すぎると感じる場合は田字格を選びます。

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

`python scripts/build.py --ids hanzi-mi`

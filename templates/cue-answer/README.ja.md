# 手がかりと答え

`cue-answer` · `learning` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![手がかりと答え](previews/a5-draft.png)

細い欄に手がかり、広い欄に確認できる答えを書きます。

## 向いている場面

**図形の対応:** `equivalent` · [two-left-narrow](../two-left-narrow/README.ja.md)

- 細い欄に自分への問いを書き、広い答え欄を隠して口頭で思い出すとき。
- 読後に短い手がかりと説明を対応させ、一人で答えられない問いを見つけるとき。

## 使い方

1. 左の細い欄に自分への短い問い、右に十分な答えを書きます。
2. 右欄を隠して問いから答えを思い出し、開いて照合します。
3. 答えが不十分だった箇所には、明確な手がかりや不足する説明を加えます。

## 記入後に見えること

概念、手がかり、思い出した答えを照合できます。


## 記入例

図の記入位置の順に示します。番号一つが一つの記入例です：

1. 日照と葉色？
2. 窓辺の葉が濃い。水やりも比べる。

![手がかりと答え 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

答えを見たままでは、文字を見分けただけで想起できたと判断しがちです。答えを明かしすぎる手がかりや根拠のない答えも自測を弱めます。

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

図形は `src/noteformats/variants.py`、文章は `src/noteformats/variant_content.py` を変更し、プロジェクトのルートで実行します：

`python scripts/build.py --ids cue-answer`

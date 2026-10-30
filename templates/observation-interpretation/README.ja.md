# 観察と解釈

`observation-interpretation` · `research` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![観察と解釈](previews/a5-draft.png)

直接の観察と仮の解釈を別の欄に分けます。

## 向いている場面

**図形の対応:** `equivalent` · [two-equal-columns](../two-equal-columns/README.ja.md)

- ワークショップで見えた行動と、その理由についての推測を分けて記録するとき。
- 物の使われ方を観察し、左に見えた現象、右に確かめる解釈を書くとき。

## 使い方

1. 左欄には見聞きした具体的な現象だけを記し、原因の推測を入れません。
2. 右欄に考えられる解釈を書き、対応する観察へ印で結びます。
3. 各解釈に必要な追加資料を確かめ、別の説明の可能性も残します。

## 記入後に見えること

資料、引用、主張、未確認事項を分けられます。


## 記入例

図の記入位置の順に示します。番号一つが一つの記入例です：

1. 観察：三人が遅刻
2. 解釈：時間が原因か。本人に確認

![観察と解釈 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

見えた行動だけでは他人の動機を確定できません。観察者の選び方や視点も記録に影響するため、別の説明と確認点を残します。

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

`python scripts/build.py --ids observation-interpretation`

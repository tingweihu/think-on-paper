# 引用と欄外メモ

`quote-side-notes` · `research` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![引用と欄外メモ](previews/a5-draft.png)

広い欄に短い引用、細い欄に出典の確認点を置きます。

## 向いている場面

**図形の対応:** `equivalent` · [two-left-narrow](../two-left-narrow/README.ja.md)

- 広い欄に文章を引用し、左の細い欄に出典ページや語の注記を添えるとき。
- 架空の掲示の文面を残し、日付や表現への疑問を脇に書くとき。

## 使い方

1. 広い欄に短い引用、細い欄に出典の確認点を置きます。
2. 右に主な内容を書き、対応する手がかりと高さをそろえます。
3. 左欄を見て探し直し、右側に十分な文脈があるか確かめます。

## 記入後に見えること

資料、引用、主張、未確認事項を分けられます。


## 記入例

図の記入位置の順に示します。番号一つが一つの記入例です：

1. 日付を確認
2. 架空の掲示：『土曜午後に開場』。

![引用と欄外メモ 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

脇の欄は短い注記向けで、文脈や出典の十分な記録の代わりにはなりません。短い引用が原意を変えないよう前後を読み返します。

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

`python scripts/build.py --ids quote-side-notes`

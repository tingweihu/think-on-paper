# 左に狭い参照欄

`two-left-narrow` · `columns` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![左に狭い参照欄](previews/a5-draft.png)

左に短い参照を置き、広い右側を文章や図に使います。

## 向いている場面

- 左に資料番号を置き、右に関係図を描くとき。
- 聞き取りの話題を左に、詳しい記録を右に書くとき。

## 使い方

1. 左欄は短い索引だけに使い、文章は入れません。
2. 右に主な内容を書き、対応する手がかりと高さをそろえます。
3. 左欄を見て探し直し、右側に十分な文脈があるか確かめます。

## 記入後に見えること

並べた記録から共通点、相違点、未確認事項を確かめられます。


## 記入例

架空の聞き取りで左に会場という語、右に入口と座席の配置の説明を置いています。

![左に狭い参照欄 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

下部の要約や主文を隠した自己テストには、コーネル式が向いています。

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

`python scripts/build.py --ids two-left-narrow`

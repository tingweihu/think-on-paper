# 右側が細い二段組

`two-right-narrow` · `columns` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![右側が細い二段組](previews/a5-draft.png)

右の細い欄に短い出典や確認点を置き、左に本文や下書きを残します。

## 向いている場面

**図形の対応:** `parameter` · [two-left-narrow](../two-left-narrow/README.ja.md)

- 左に読書メモを書き、右の細い欄にページ番号と調べる語だけを置くとき。
- 左に会場図を描き、右欄へ寸法の疑問や確認印を集めるとき。

## 使い方

1. 左の広い欄に本文や図、右の細い欄にページ番号・出典記号・短い問いを書きます。
2. 左右の対応に同じ印を使い、長文を右欄へ詰め込まないようにします。
3. 右欄の問いを一つずつ確かめ、未解決のものに印を残します。

## 記入後に見えること

並べた記録から共通点、相違点、未確認事項を確かめられます。


## 記入例

図の記入位置の順に示します。番号一つが一つの記入例です：

1. 会場
2. 入口は棚の近く、席は窓辺。

![右側が細い二段組 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

下部の要約や主文を隠した自己テストには、コーネル式が向いています。 小さなマスは短い語句向けで、長い文章には向きません。

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

`python scripts/build.py --ids two-right-narrow`

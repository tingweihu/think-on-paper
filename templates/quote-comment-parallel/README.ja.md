# 引用とコメント

`quote-comment-parallel` · `research` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![引用とコメント](previews/a5-draft.png)

架空の引用と確認が必要なコメントを左右に分けます。

## 向いている場面

**図形の対応:** `equivalent` · [two-equal-columns](../two-equal-columns/README.ja.md)

- 一方の欄に記事の原文、もう一方に自分のコメントや問いを対応させるとき。
- 架空の聞き取りの引用と分析メモを並べ、引用へ解釈を混ぜないようにするとき。

## 使い方

1. 架空の引用と確認が必要なコメントを左右に分けます。
2. 対応する内容を近い高さに置き、必要なら矢印で結びます。
3. 片側だけにある項目を見つけ、確認が必要な資料を記します。

## 記入後に見えること

資料、引用、主張、未確認事項を分けられます。


## 記入例

図の記入位置の順に示します。番号一つが一つの記入例です：

1. 引用：『土曜午後に開場』
2. 注記：日付と出典を確認

![引用とコメント 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

引用の隣に置いたコメントは、原著者がその解釈に同意することを示しません。引用と要約を区別し、複数段落の論証を文脈のない一文に切り分けないようにします。

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

`python scripts/build.py --ids quote-comment-parallel`

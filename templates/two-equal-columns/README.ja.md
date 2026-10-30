# 等幅の二段組

`two-equal-columns` · `columns` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![等幅の二段組](previews/a5-draft.png)

同じ重みの二種類の内容を左右に置き、行ごとや全体で比べます。

## 向いている場面

- 同じ問いについて二つの短い記事を比べるとき。
- 原文と自分の書き換えを左右に置くとき。

## 使い方

1. 左右が何を表すか決め、自分のメモに記します。
2. 対応する内容を近い高さに置き、必要なら矢印で結びます。
3. 片側だけにある項目を見つけ、確認が必要な資料を記します。

## 記入後に見えること

並べた記録から共通点、相違点、未確認事項を確かめられます。


## 記入例

架空の展示会の紙の案内と口頭案内を並べ、得られる情報や質問のしやすさを比べています。

![等幅の二段組 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

片側が短い手がかりで、もう一方が長文なら等幅は余白を無駄にします。

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

`python scripts/build.py --ids two-equal-columns`

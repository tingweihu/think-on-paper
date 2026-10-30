# T字比較

`t-comparison` · `comparison` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![T字比較](previews/a5-draft.png)

上に共通の問いを書き、下の左右に二つの答えを分けます。

## 向いている場面

**図形の対応:** `parameter` · [two-equal-columns](../two-equal-columns/README.ja.md)

- 同じ催しに対する二つの会場を比べるとき。
- 一つの主張への賛否の理由を整理するとき。

## 使い方

1. 上段に比べる問いを明確に書きます。
2. 左右に選択肢や立場を一つずつ割り当てます。
3. 根拠を順に書き、足りない情報を探します。

## 記入後に見えること

同じ条件で選択肢を見比べ、一つの印象だけで決めることを避けられます。


## 記入例

架空の読書会の会場を問い、図書館と屋外の東屋を左右で比べています。

![T字比較 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

三案以上や数値の重み付けにはT字だけでは足りません。

## ダウンロード

- [文字なしSVG](exports/a5-draft/blank.svg)
- [文字なしPDF](exports/a5-draft/blank.pdf)
- [左上に英語名があるPDF](exports/a5-draft/titled.pdf)
- [濃い線の文字なしPDF](exports/a5-contrast/blank.pdf)
- [濃い線のSVG](exports/a5-contrast/blank.svg)

英語名は表題付きPDFだけに印刷され、文字なし版は自由な記入に使えます。

用紙サイズ：A5（148 × 210 mm）。設定ファイル：`a5-draft`。

## 由来と状態

伝統的な形式の応用 · 詳しい由来の記録： [manifest.json](manifest.json)  
[MITライセンスの範囲](../../LICENSE-SCOPE.md)

[三言語の用語集](../../docs/ja/glossary.md)

## 変更と再生成

`profiles/a5-draft.json` または `src/noteformats/layouts/` の描画関数を変更し、プロジェクトのルートで実行します：

`python scripts/build.py --ids t-comparison`

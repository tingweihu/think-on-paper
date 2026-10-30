# 二中心のバブル比較

`double-bubble` · `comparison` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![二中心のバブル比較](previews/a5-draft.png)

二つの主題を共通の特徴と固有の特徴につなげます。

## 向いている場面

- 二種類の案内の共通目的と違いを比べるとき。
- 二つの物の同じ機能と異なる使い方を整理するとき。

## 使い方

1. 左右の大きな円に二つの主題を書きます。
2. 上下の泡に両者に共通する特徴を書きます。
3. 外側の小さな泡に固有の特徴を置き、各線が妥当か確かめます。

## 記入後に見えること

同じ条件で選択肢を見比べ、一つの印象だけで決めることを避けられます。


## 記入例

紙の案内と口頭案内は経路と情報を共有し、保存できることと質問できることがそれぞれの特徴です。

![二中心のバブル比較 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

泡が小さく短い語しか入りません。詳しい根拠や数値には表を使います。

## ダウンロード

- [文字なしSVG](exports/a5-draft/blank.svg)
- [文字なしPDF](exports/a5-draft/blank.pdf)
- [左上に英語名があるPDF](exports/a5-draft/titled.pdf)
- [濃い線の文字なしPDF](exports/a5-contrast/blank.pdf)
- [濃い線のSVG](exports/a5-contrast/blank.svg)

英語名は表題付きPDFだけに印刷され、文字なし版は自由な記入に使えます。

用紙サイズ：A5（148 × 210 mm）。設定ファイル：`a5-draft`。

## 由来と状態

既存の方法を配置に応用 · 詳しい由来の記録： [manifest.json](manifest.json)  
[MITライセンスの範囲](../../LICENSE-SCOPE.md)

[三言語の用語集](../../docs/ja/glossary.md)

## 変更と再生成

`profiles/a5-draft.json` または `src/noteformats/layouts/` の描画関数を変更し、プロジェクトのルートで実行します：

`python scripts/build.py --ids double-bubble`

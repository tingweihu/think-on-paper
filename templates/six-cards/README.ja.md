# 六枚の独立カード

`six-cards` · `cards` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![六枚の独立カード](previews/a5-draft.png)

候補の考えを一枚ずつ独立したカードに置き、比べたり並べたりします。 図形の変更： 独立カード数: 6.

## 向いている場面

**図形の対応:** `parameter` · [four-cards](../four-cards/README.ja.md)

- 六人の聞き取りを一人一枚のカードにまとめ、共通点を見返すとき。
- 章を読んだ後、六つの概念を一マス一項の定義と短い例で整理するとき。

## 使い方

1. 各カードを案か観点に割り当て、一枚に比較できる単位を一つ置きます。
2. 記入例を参考に、領域の順で記します：1「図書館の十席」；2「短い本を四冊」；3「金曜までに案内」；4「土曜の午後」；5「進行役を二人」；6「感想を集める」
3. 各領域を読み返し、未確認の点と次の行動を記します。

## 記入後に見えること

項目を分けて、並べ替えや比較、選択ができます。


## 記入例

図の記入位置の順に示します。番号一つが一つの記入例です：

1. 図書館の十席
2. 短い本を四冊
3. 金曜までに案内
4. 土曜の午後
5. 進行役を二人
6. 感想を集める

![六枚の独立カード 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

六枚のカードには一項ずつ要約できますが、配置だけでは順序や因果を示せません。聞き取りの全文やカード間の関係は別に記録します。

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

`python scripts/build.py --ids six-cards`

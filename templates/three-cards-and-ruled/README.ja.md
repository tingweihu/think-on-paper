# 三カードと横罫のまとめ

`three-cards-and-ruled` · `hybrid` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![三カードと横罫のまとめ](previews/a5-draft.png)

上に三つの案を並べ、下に比較と選択理由を書きます。

## 向いている場面

- 講座の三つの題材を比べるとき。
- 三つの短い資料から共通の話題を探すとき。

## 使い方

1. 上の各カードに独立した案を一つ置きます。
2. 下ではカードの書き写しではなく、共通点と違いを書きます。
3. 選択理由か未解決の問いを明確にします。

## 記入後に見えること

図、短い記録、結論を分けながら関係づけられます。


## 記入例

架空の催しで講話、共読、工作を比べ、下には共読を試す理由と会場の確認点を書きます。

![三カードと横罫のまとめ 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

三つの案が同じ重みだとは限りません。数値で判断する場合はデータ表を使います。

## ダウンロード

- [文字なしSVG](exports/a5-draft/blank.svg)
- [文字なしPDF](exports/a5-draft/blank.pdf)
- [左上に英語名があるPDF](exports/a5-draft/titled.pdf)
- [濃い線の文字なしPDF](exports/a5-contrast/blank.pdf)
- [濃い線のSVG](exports/a5-contrast/blank.svg)

英語名は表題付きPDFだけに印刷され、文字なし版は自由な記入に使えます。

用紙サイズ：A5（148 × 210 mm）。設定ファイル：`a5-draft`。

## 由来と状態

本プロジェクトの独自レイアウト · 詳しい由来の記録： [manifest.json](manifest.json)  
[MITライセンスの範囲](../../LICENSE-SCOPE.md)

[三言語の用語集](../../docs/ja/glossary.md)

## 変更と再生成

`profiles/a5-draft.json` または `src/noteformats/layouts/` の描画関数を変更し、プロジェクトのルートで実行します：

`python scripts/build.py --ids three-cards-and-ruled`

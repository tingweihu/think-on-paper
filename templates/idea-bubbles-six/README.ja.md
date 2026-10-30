# 六つの吹き出しの発想図

`idea-bubbles-six` · `ideation` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![六つの吹き出しの発想図](previews/a5-draft.png)

一つの話題の周囲に六つの異なる案を置き、まだ順位を決めません。

## 向いている場面

**図形の対応:** `parameter` · [flower-eight](../flower-eight/README.ja.md)

- 同じ催しのテーマに六つの始め方を集め、まだ点数を付けないとき。
- 物の再利用を問いにして六つの用途案を広げ、その後で試作する方向を選ぶとき。

## 使い方

1. 中心に主題、外側の円に重複しない観点を置きます。
2. 記入例を参考に、領域の順で記します：1「地域菜園」；2「栽培」；3「休憩」；4「学習」；5「共有」；6「維持」；7「道具」
3. 各領域を読み返し、未確認の点と次の行動を記します。

## 記入後に見えること

複数の案と、次に選ぶための基準が残ります。


## 記入例

図の記入位置の順に示します。番号一つが一つの記入例です：

1. 地域菜園
2. 栽培
3. 休憩
4. 学習
5. 共有
6. 維持
7. 道具

![六つの吹き出しの発想図 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

六つの円は候補を残す場所で、実現性・重要度・網羅性を示しません。円が埋まったことを結論とせず、選ぶ前に条件を比べます。

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

図形は `src/noteformats/variants.py`、文章は `src/noteformats/variant_content.py` を変更し、プロジェクトのルートで実行します：

`python scripts/build.py --ids idea-bubbles-six`

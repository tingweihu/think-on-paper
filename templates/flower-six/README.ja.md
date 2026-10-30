# 六つの花びらの発想図

`flower-six` · `mandala` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![六つの花びらの発想図](previews/a5-draft.png)

中心の話題から周囲の六つの吹き出しへ考えを広げます。 図形の変更： 外側の円数: 6.

## 向いている場面

**図形の対応:** `parameter` · [flower-eight](../flower-eight/README.ja.md)

- 人物名を中心に、動機・習慣・背景など六つの面を花弁に広げるとき。
- 地域の催しを中心に置き、異なる六つの参加ニーズを花弁に分けるとき。

## 使い方

1. 中心に主題、外側の円に重複しない観点を置きます。
2. 記入例を参考に、領域の順で記します：1「地域菜園」；2「栽培」；3「休憩」；4「学習」；5「共有」；6「維持」；7「道具」
3. 各領域を読み返し、未確認の点と次の行動を記します。

## 記入後に見えること

中心のテーマから次に調べる方向を広げられます。


## 記入例

図の記入位置の順に示します。番号一つが一つの記入例です：

1. 地域菜園
2. 栽培
3. 休憩
4. 学習
5. 共有
6. 維持
7. 道具

![六つの花びらの発想図 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

六つの花弁は観点を広げるためのもので、輪郭の重なりは集合の共通部分や因果を示しません。所属規則や関係を明示するには表や概念網を使います。

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

`python scripts/build.py --ids flower-six`

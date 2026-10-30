# 無地のページ

`blank` · `foundation` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![無地のページ](previews/a5-draft.png)

文字、絵、配置の関係をすべて書き手が決められる形式です。

## 向いている場面

- 考えの形がまだ決まらず、絵と短い言葉を混ぜたいとき。
- 会議で手がかりを素早く記録し、あとで結び直すとき。

## 使い方

1. 読む順番を固定せず、書き始める場所を決めます。
2. 距離、囲み、矢印で関連があると思う内容を示します。
3. 重要な印に短い名前を付け、未解決の問いは次のページに移します。

## 記入後に見えること

読み返せる連続した記録や下書きと、未確認の点が残ります。


## 記入例

架空の地域菜園について、植物、道具、世話の時間を別の位置に書き、関係を結ぶ例です。空白版には文字がありません。

![無地のページ 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

一定の行間、正確な表、複数人で同じ欄を埋める書式には手がかりが足りません。

## ダウンロード

- [文字なしSVG](exports/a5-draft/blank.svg)
- [文字なしPDF](exports/a5-draft/blank.pdf)
- [左上に英語名があるPDF](exports/a5-draft/titled.pdf)
- [濃い線の文字なしPDF](exports/a5-contrast/blank.pdf)
- [濃い線のSVG](exports/a5-contrast/blank.svg)

英語名は表題付きPDFだけに印刷され、文字なし版は自由な記入に使えます。

用紙サイズ：A5（148 × 210 mm）。設定ファイル：`a5-draft`。

## 由来と状態

伝統的な練習紙の応用 · 詳しい由来の記録： [manifest.json](manifest.json)  
[MITライセンスの範囲](../../LICENSE-SCOPE.md)

[三言語の用語集](../../docs/ja/glossary.md)

## 変更と再生成

`profiles/a5-draft.json` または `src/noteformats/layouts/` の描画関数を変更し、プロジェクトのルートで実行します：

`python scripts/build.py --ids blank`

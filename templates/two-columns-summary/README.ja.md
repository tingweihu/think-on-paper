# 二欄とまとめ

`two-columns-summary` · `columns` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![二欄とまとめ](previews/a5-draft.png)

上で二つの見方を分け、下の全幅欄で統合した考えを書きます。

## 向いている場面

- 二つの資料を比べて暫定的な共通結論を書くとき。
- 二案を話し合い、確認が必要な折衷案を整理するとき。

## 使い方

1. 上の左右に資料や案を一つずつ割り当てます。
2. 比べられる点や違いを近い高さに書きます。
3. 下欄に今言える結論と未解決の問いを自分の言葉で書きます。

## 記入後に見えること

並べた記録から共通点、相違点、未確認事項を確かめられます。


## 記入例

架空の読書会で屋内と屋外を比べ、天候と代替場所の確認を下欄にまとめています。

![二欄とまとめ 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

左右の量が大きく違うと片側が余り、下欄にも長い報告は入りません。

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

`python scripts/build.py --ids two-columns-summary`

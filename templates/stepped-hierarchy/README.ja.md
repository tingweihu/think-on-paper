# 段階式の階層メモ

`stepped-hierarchy` · `hierarchy` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [一覧へ戻る](../../docs/ja/catalog.md)

![段階式の階層メモ](previews/a5-draft.png)

抽象的な意図を一段ずつ具体的な行動へ変えます。

## 向いている場面

- 催しの目的を作業項目に落とすとき。
- 大きな主張から例と確認事項へ進むとき。

## 使い方

1. 最初の段に全体の目標を書きます。
2. 次の段ごとに具体性を一段だけ増やし、上段との関係を保ちます。
3. 最後は観察できる行動を書き、上段から導けるか確かめます。

## 記入後に見えること

目的や話題の階層と、抜けている要素が見えます。


## 記入例

架空の読書会で『読書を共有』から『毎月集まる』『交代で質問』『部屋を予約』へ進みます。

![段階式の階層メモ 記入例](examples/ja.svg)

[SVG](examples/ja.svg)

## 向いていない場面

階段は必然的な順序に見えやすいため、並行する枝には樹形図や欄を使います。

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

`python scripts/build.py --ids stepped-hierarchy`

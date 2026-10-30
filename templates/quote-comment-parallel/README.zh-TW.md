# 引文與評論對照

`quote-comment-parallel` · `research` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![引文與評論對照](previews/a5-draft.png)

左右並列虛構引文與自己的查證評論。

## 適合情境

**幾何對照:** `equivalent` · [two-equal-columns](../two-equal-columns/README.zh-TW.md)

- 在一欄保留文章原句，另一欄逐項寫下自己的評論與疑問。
- 對照虛構訪談摘句與分析備註，避免把解讀混進引文。

## 使用步驟

1. 左右並列虛構引文與自己的查證評論。
2. 在相近高度放對應內容，必要時以箭頭連結。
3. 回看哪些項目只在一側出現，記下需要補查的來源。

## 整理後可得到

分開來源、引文、主張與待查問題。


## 實際填寫示例

依圖中填寫位置順序列出，每個編號是一筆示例條目：

1. 引文：『週六下午開放』
2. 評論：日期與來源待確認

![引文與評論對照 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

並排評論不代表原作者同意你的解讀；引文與改寫須清楚區分，跨多段的論證也不宜拆成失去脈絡的單句。

## 下載

- [無字 SVG](exports/a5-draft/blank.svg)
- [無字 PDF](exports/a5-draft/blank.pdf)
- [左上角英文名稱 PDF](exports/a5-draft/titled.pdf)
- [深色墨線無字 PDF](exports/a5-contrast/blank.pdf)
- [深色墨線 SVG](exports/a5-contrast/blank.svg)

英文名稱只印在標題版 PDF；無字版仍適合自由列印與改作。

頁面尺寸：A5（148 × 210 mm）；設定檔：`a5-draft`。

## 來源與狀態

通用幾何結構 · 詳細來源紀錄見 [manifest.json](manifest.json)  
[MIT 授權範圍](../../LICENSE-SCOPE.md)

[三語術語表](../../docs/zh-TW/glossary.md)

## 修改與重新生成

調整 `src/noteformats/variants.py` 的幾何或 `src/noteformats/variant_content.py` 的文字，再於專案根目錄執行：

`python scripts/build.py --ids quote-comment-parallel`

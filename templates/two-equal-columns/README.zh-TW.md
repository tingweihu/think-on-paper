# 等寬雙欄

`two-equal-columns` · `columns` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![等寬雙欄](previews/a5-draft.png)

讓兩組同等重要的內容並排，逐行或整體對照。

## 適合情境

- 比較兩篇短文對同一問題的說法。
- 把一段原文與自己的改寫放在左右兩邊。

## 使用步驟

1. 先決定左右各代表什麼，寫在你自己的筆記中。
2. 在相近高度放對應內容，必要時以箭頭連結。
3. 回看哪些項目只在一側出現，記下需要補查的來源。

## 整理後可得到

對照分欄內容，找出相同點、差異與待查證資訊。


## 實際填寫示例

示例把虛構展覽的紙本導覽與口頭導覽並列，對照可取得的資訊與疑問。

![等寬雙欄 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

若一側只是短提示、另一側是長篇內容，等寬分配會浪費空間。

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

修改 `profiles/a5-draft.json` 或 `src/noteformats/layouts/` 內對應的繪圖函式，再於專案根目錄執行：

`python scripts/build.py --ids two-equal-columns`

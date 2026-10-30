# 窄左欄主筆記

`two-left-narrow` · `columns` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![窄左欄主筆記](previews/a5-draft.png)

窄欄放參照線索，寬欄保留大幅連續書寫或作圖空間。

## 適合情境

- 閱讀資料時左邊放來源代碼，右邊畫關係圖。
- 訪談整理時左邊記主題，右邊寫完整摘記。

## 使用步驟

1. 先決定左欄只收短索引，不放完整句子。
2. 在右欄記錄主要內容，對應左欄的索引保持相近高度。
3. 回顧時以左欄快速定位，確認右欄仍有足夠脈絡。

## 整理後可得到

對照分欄內容，找出相同點、差異與待查證資訊。


## 實際填寫示例

示例以虛構訪談為題，左欄放『場地』線索，右欄記受訪者描述的空間安排。

![窄左欄主筆記 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

需要頁末總結與遮住主文自測時，康乃爾版型更適合。

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

`python scripts/build.py --ids two-left-narrow`

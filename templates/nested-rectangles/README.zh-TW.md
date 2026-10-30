# 同心矩形範圍圖

`nested-rectangles` · `hierarchy` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![同心矩形範圍圖](previews/a5-draft.png)

由外到內記錄四個包含關係，辨認範圍如何逐步縮小。

## 適合情境

- 從城市、街區、場地一路聚焦到一間教室。
- 將研究題目由大領域逐步界定成單一問題。

## 使用步驟

1. 最外圈寫最大的範圍。
2. 往內每圈只縮小一層，不能跳到無關分類。
3. 在最內圈寫實際要處理的對象，回看邊界是否明確。

## 整理後可得到

區分上位目標與下位要素，檢查是否遺漏。


## 實際填寫示例

虛構活動從城市、社區、圖書館縮到一間閱讀室，讓場地討論有清楚範圍。

![同心矩形範圍圖 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

同心結構只說明包含，不能顯示並列類別或時間順序。

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

`python scripts/build.py --ids nested-rectangles`

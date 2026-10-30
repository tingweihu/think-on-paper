# 等距點陣

`dot-standard` · `grid-dot` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![等距點陣](previews/a5-draft.png)

以淡點輔助對齊，同時保留比方格更開放的書寫感。

## 適合情境

- 自由畫框線與箭頭，但仍希望大致對齊。
- 在短筆記旁加入小尺寸示意圖。

## 使用步驟

1. 把點當作定位參考，不必每個點都用到。
2. 先寫主題，再以點連成需要的框或線。
3. 回看時檢查畫出的結構是否比文字更清楚。

## 整理後可得到

用格線或點位對齊物件、數量與相對位置。


## 實際填寫示例

示例把虛構社區活動的場地、材料與人員畫成三個對齊的短區塊。

![等距點陣 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

需要明確格界或連續橫線時，只有點可能不夠醒目。

## 下載

- [無字 SVG](exports/a5-draft/blank.svg)
- [無字 PDF](exports/a5-draft/blank.pdf)
- [左上角英文名稱 PDF](exports/a5-draft/titled.pdf)
- [深色墨線無字 PDF](exports/a5-contrast/blank.pdf)
- [深色墨線 SVG](exports/a5-contrast/blank.svg)

英文名稱只印在標題版 PDF；無字版仍適合自由列印與改作。

頁面尺寸：A5（148 × 210 mm）；設定檔：`a5-draft`。

## 來源與狀態

傳統書寫紙改編 · 詳細來源紀錄見 [manifest.json](manifest.json)  
[MIT 授權範圍](../../LICENSE-SCOPE.md)

[三語術語表](../../docs/zh-TW/glossary.md)

## 修改與重新生成

修改 `profiles/a5-draft.json` 或 `src/noteformats/layouts/` 內對應的繪圖函式，再於專案根目錄執行：

`python scripts/build.py --ids dot-standard`

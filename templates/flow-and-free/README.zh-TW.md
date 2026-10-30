# 流程加自由補圖

`flow-and-free` · `hybrid` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![流程加自由補圖](previews/a5-draft.png)

上方固定四個主要步驟，下方補畫例外路徑與現場觀察。

## 適合情境

- 規劃活動報名的主要流程及例外。
- 記錄借書流程後補上讀者可能遇到的問題。

## 使用步驟

1. 上方四格依順序寫主要動作。
2. 下方留白畫出例外、回頭路或現場情境。
3. 核對補圖是否改變原流程，必要時回上方修訂。

## 整理後可得到

把圖、短記與結論放在各自區域，再檢查關係。


## 實際填寫示例

虛構借書流程寫找書、借出、閱讀、歸還；下方畫逾期或找不到書時的分支。

![流程加自由補圖 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

上方四步只是概要；複雜分支和責任歸屬應用完整流程或泳道圖。

## 下載

- [無字 SVG](exports/a5-draft/blank.svg)
- [無字 PDF](exports/a5-draft/blank.pdf)
- [左上角英文名稱 PDF](exports/a5-draft/titled.pdf)
- [深色墨線無字 PDF](exports/a5-contrast/blank.pdf)
- [深色墨線 SVG](exports/a5-contrast/blank.svg)

英文名稱只印在標題版 PDF；無字版仍適合自由列印與改作。

頁面尺寸：A5（148 × 210 mm）；設定檔：`a5-draft`。

## 來源與狀態

本專案原創版面 · 詳細來源紀錄見 [manifest.json](manifest.json)  
[MIT 授權範圍](../../LICENSE-SCOPE.md)

[三語術語表](../../docs/zh-TW/glossary.md)

## 修改與重新生成

修改 `profiles/a5-draft.json` 或 `src/noteformats/layouts/` 內對應的繪圖函式，再於專案根目錄執行：

`python scripts/build.py --ids flow-and-free`

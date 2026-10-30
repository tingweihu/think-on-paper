# 細方格

`grid-fine` · `grid-dot` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![細方格](previews/a5-draft.png)

用等距方格對齊短語、簡圖與比例草稿。 本款的幾何變化： 方格間距: 3 mm.

## 適合情境

**幾何對照:** `parameter` · [grid-standard](../grid-standard/README.zh-TW.md)

- 在較細的方格上試畫小型包裝的展開草圖，保留尺寸待核記號。
- 將密集但簡短的符號逐格排列，檢查圖樣是否重複一致。

## 使用步驟

1. 先決定一格在這頁代表的長度或一個項目。
2. 沿格線放置線條或短語，保留相鄰格作註解。
3. 最後檢查比例假設，必要時在紙外記下實際尺寸。

## 整理後可得到

用格線或點位對齊物件、數量與相對位置。


## 實際填寫示例

示例用幾格表示虛構閱讀角的桌、椅與通道，旁邊記下要量測的寬度。 示例以虛構資料在對應區域放入短語，示意填寫位置；不是實測或完整研究結論。

![細方格 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

3 mm 細格適合短符號與局部草圖，不適合每格寫長詞；若要表達實際尺寸，仍須另訂比例與單位。

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

調整 `src/noteformats/variants.py` 的幾何或 `src/noteformats/variant_content.py` 的文字，再於專案根目錄執行：

`python scripts/build.py --ids grid-fine`

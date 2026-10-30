# 工程主線方格

`engineering-grid` · `geometry` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![工程主線方格](previews/a5-draft.png)

用等距方格對齊短語、簡圖與比例草稿。 本款的幾何變化： 每五格有較明顯的主線。

## 適合情境

**幾何對照:** `parameter` · [grid-standard](../grid-standard/README.zh-TW.md)

- 畫機構草圖時以每五格的主線定位，細格補充局部比例。
- 在同頁比較零件外形，利用粗細格線分辨整體與細部單位。

## 使用步驟

1. 先決定一格在這頁代表的長度或一個項目。
2. 沿格線放置線條或短語，保留相鄰格作註解。
3. 最後檢查比例假設，必要時在紙外記下實際尺寸。

## 整理後可得到

看出方向、比例或空間配置中需要再測量之處。


## 實際填寫示例

示例用幾格表示虛構閱讀角的桌、椅與通道，旁邊記下要量測的寬度。 示例以虛構資料在對應區域放入短語，示意填寫位置；不是實測或完整研究結論。

![工程主線方格 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

每五格的主線只是定位輔助，不自動提供工程公差、比例尺或尺寸標註；需要製作依據時應另附完整規格。

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

`python scripts/build.py --ids engineering-grid`

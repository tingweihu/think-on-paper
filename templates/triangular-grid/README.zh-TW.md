# 三角網格

`triangular-grid` · `geometry` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![三角網格](previews/a5-draft.png)

用三方向等距線條草擬斜向構造與三角分割。

## 適合情境

- 畫三角形拼接的材料配置。
- 比較不同斜向支撐的草圖。

## 使用步驟

1. 先選一個三角邊長代表的暫定尺度。
2. 沿三個線向畫輪廓，避免把縮圖當精密量測。
3. 在格外記下需實測的角度與尺寸。

## 整理後可得到

看出方向、比例或空間配置中需要再測量之處。


## 實際填寫示例

示例用三角網格標出虛構展架的三個支撐點和一條斜撐，旁邊保留待測尺寸。

![三角網格 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

長篇筆記或矩形表格不易沿三角格閱讀；尚未標定的網格不能替代製圖工具。

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

`python scripts/build.py --ids triangular-grid`

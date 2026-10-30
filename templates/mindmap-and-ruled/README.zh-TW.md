# 概念圖加橫線筆記

`mindmap-and-ruled` · `hybrid` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![概念圖加橫線筆記](previews/a5-draft.png)

上半快速展開四個方向，下半把其中一個方向寫成可讀的說明。

## 適合情境

- 讀書時先找主題的四個面向，再寫一段摘要。
- 規劃活動時先發想，後寫出要試的方案。

## 使用步驟

1. 上半中心寫主題，四圈放不同方向。
2. 選最值得追查的一圈，在下半寫出具體說明。
3. 回頭檢查文字是否超出圖中原本假設。

## 整理後可得到

把圖、短記與結論放在各自區域，再檢查關係。


## 實際填寫示例

虛構講座主題是『地方故事』，四圈是訪談、照片、地圖、分享；下半寫一段訪談試辦方式。

![概念圖加橫線筆記 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

小圈只能寫短詞；若有八個以上方向，先用完整概念圖。

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

`python scripts/build.py --ids mindmap-and-ruled`

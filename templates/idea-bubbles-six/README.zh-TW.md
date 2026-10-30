# 六泡發想圖

`idea-bubbles-six` · `ideation` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![六泡發想圖](previews/a5-draft.png)

把同一主題周圍六個不同構想分開記錄，暫不排序。

## 適合情境

**幾何對照:** `parameter` · [flower-eight](../flower-eight/README.zh-TW.md)

- 為同一個活動主題收集六個不同的開場構想，先不評分。
- 圍繞物件再利用的問題寫六種可能用途，之後再挑可試做的方向。

## 使用步驟

1. 中央寫主題，外圈每個圓放一個不同面向，避免重複詞。
2. 參考本頁示例，各區依序記錄：1「社區花園」；2「種植」；3「休息」；4「學習」；5「分享」；6「維護」；7「工具」
3. 回看各區，標記仍待查證的內容，再決定下一步。

## 整理後可得到

保留多種方案並說明下一輪篩選依據。


## 實際填寫示例

依圖中填寫位置順序列出，每個編號是一筆示例條目：

1. 社區花園
2. 種植
3. 休息
4. 學習
5. 分享
6. 維護
7. 工具

![六泡發想圖 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

六個氣泡只保留候選想法，不表示可行性、重要性或完整範圍；挑選方案前仍須比較條件，不能以填滿氣泡作為結論。

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

調整 `src/noteformats/variants.py` 的幾何或 `src/noteformats/variant_content.py` 的文字，再於專案根目錄執行：

`python scripts/build.py --ids idea-bubbles-six`

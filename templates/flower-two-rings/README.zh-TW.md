# 雙環概念花

`flower-two-rings` · `mandala` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![雙環概念花](previews/a5-draft.png)

內圈寫六個主要方向，外圈各接一個更具體的短詞。

## 適合情境

- 先列活動六種需求，再補具體行動。
- 研究主題分六面向後，給每面向一個待查例子。

## 使用步驟

1. 中央寫核心問題。
2. 內圈沿六方向寫大類，外圈對應寫下一層細節。
3. 逐方向檢查內外是否真有從屬關係，必要時改寫。

## 整理後可得到

從中心主題展開多個可再追問的面向。


## 實際填寫示例

示例以虛構讀書會為中心，內圈記場地、選書、時間、邀請、材料、討論，外圈各補一個短例。

![雙環概念花 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

每個泡泡很小，只適合短詞；若某一方向需要多個細節，改用獨立頁。

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

`python scripts/build.py --ids flower-two-rings`

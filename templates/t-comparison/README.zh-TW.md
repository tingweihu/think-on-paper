# T 形比較

`t-comparison` · `comparison` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![T 形比較](previews/a5-draft.png)

先寫同一個問題，再把兩種答案分在下方左右。

## 適合情境

**幾何對照:** `parameter` · [two-equal-columns](../two-equal-columns/README.zh-TW.md)

- 比較兩種場地對同一活動的影響。
- 整理一個主張的支持與反對理由。

## 使用步驟

1. 在上方寫清楚要比較的問題。
2. 左、右各指定一個選項或立場。
3. 逐項寫出根據，回看哪些內容仍缺資料。

## 整理後可得到

用同一組條件逐一比較選項，避免只憑單一印象。


## 實際填寫示例

示例上方問虛構讀書會應在何處辦，左右比較圖書館與戶外亭。

![T 形比較 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

超過兩個方案或需要數值權重時，T 形分區不夠。

## 下載

- [無字 SVG](exports/a5-draft/blank.svg)
- [無字 PDF](exports/a5-draft/blank.pdf)
- [左上角英文名稱 PDF](exports/a5-draft/titled.pdf)
- [深色墨線無字 PDF](exports/a5-contrast/blank.pdf)
- [深色墨線 SVG](exports/a5-contrast/blank.svg)

英文名稱只印在標題版 PDF；無字版仍適合自由列印與改作。

頁面尺寸：A5（148 × 210 mm）；設定檔：`a5-draft`。

## 來源與狀態

傳統格式改編 · 詳細來源紀錄見 [manifest.json](manifest.json)  
[MIT 授權範圍](../../LICENSE-SCOPE.md)

[三語術語表](../../docs/zh-TW/glossary.md)

## 修改與重新生成

修改 `profiles/a5-draft.json` 或 `src/noteformats/layouts/` 內對應的繪圖函式，再於專案根目錄執行：

`python scripts/build.py --ids t-comparison`

# 雙欄加總結

`two-columns-summary` · `columns` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![雙欄加總結](previews/a5-draft.png)

先保留兩邊的不同觀點，再在底部寫一個整合結論。

## 適合情境

- 比較兩份資料後寫出暫時的共同結論。
- 討論兩種方案，再整理尚待驗證的折衷方向。

## 使用步驟

1. 上方左右各寫一個來源或方案。
2. 沿同一高度記下可比較的要點與差異。
3. 在下方用自己的話寫目前能支持的結論及未解問題。

## 整理後可得到

對照分欄內容，找出相同點、差異與待查證資訊。


## 實際填寫示例

示例上方比較虛構讀書會的室內與戶外場地，底部寫出天候是選址的待查條件。

![雙欄加總結 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

若兩邊內容長度差異懸殊，等寬上欄可能浪費一側；總結帶也不適合長篇報告。

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

`python scripts/build.py --ids two-columns-summary`

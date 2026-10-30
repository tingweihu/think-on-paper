# 線索與回答

`cue-answer` · `learning` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![線索與回答](previews/a5-draft.png)

窄欄放提問線索，寬欄放可查證的回答。

## 適合情境

**幾何對照:** `equivalent` · [two-left-narrow](../two-left-narrow/README.zh-TW.md)

- 把自測問題放在窄欄，遮住較寬的答案區後練習口頭回想。
- 閱讀後用短提示詞對照完整解釋，找出不能自行回答的題目。

## 使用步驟

1. 左側窄欄寫一個能自問的短問題，右側寫完整答案。
2. 遮住右欄，僅看問題回想答案，再打開核對。
3. 把回答不完整的地方改寫成更明確的提示或補充說明。

## 整理後可得到

把概念、線索與回想結果相互對照。


## 實際填寫示例

依圖中填寫位置順序列出，每個編號是一筆示例條目：

1. 葉色與光照？
2. 窗邊葉較深；也須控制澆水量。

![線索與回答 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

答案欄若一直可見，容易把辨認文字當成獨立回想；提示過於明顯或答案缺少來源，也會讓自測結果失真。

## 下載

- [無字 SVG](exports/a5-draft/blank.svg)
- [無字 PDF](exports/a5-draft/blank.pdf)
- [左上角英文名稱 PDF](exports/a5-draft/titled.pdf)
- [深色墨線無字 PDF](exports/a5-contrast/blank.pdf)
- [深色墨線 SVG](exports/a5-contrast/blank.svg)

英文名稱只印在標題版 PDF；無字版仍適合自由列印與改作。

頁面尺寸：A5（148 × 210 mm）；設定檔：`a5-draft`。

## 來源與狀態

通用幾何結構 · 詳細來源紀錄見 [manifest.json](manifest.json)  
[MIT 授權範圍](../../LICENSE-SCOPE.md)

[三語術語表](../../docs/zh-TW/glossary.md)

## 修改與重新生成

調整 `src/noteformats/variants.py` 的幾何或 `src/noteformats/variant_content.py` 的文字，再於專案根目錄執行：

`python scripts/build.py --ids cue-answer`

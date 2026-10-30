# 右窄欄筆記

`two-right-narrow` · `columns` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![右窄欄筆記](previews/a5-draft.png)

將短來源與待查問題放在右側窄欄，左側留給連續筆記或草圖。

## 適合情境

**幾何對照:** `parameter` · [two-left-narrow](../two-left-narrow/README.zh-TW.md)

- 左側寫閱讀筆記，右側窄欄只放頁碼與待查詞。
- 在左側畫場地草圖，右側集中列出尺寸疑問與核對記號。

## 使用步驟

1. 左側大欄記主筆記或草圖，右側窄欄記頁碼、來源代碼或短問題。
2. 用相同記號對應左右內容，避免長句擠進右欄。
3. 完成後逐項核對右欄的問題，將仍待查的項目留下記號。

## 整理後可得到

對照分欄內容，找出相同點、差異與待查證資訊。


## 實際填寫示例

依圖中填寫位置順序列出，每個編號是一筆示例條目：

1. 場地
2. 入口靠近書架，座位在窗邊。

![右窄欄筆記 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

需要頁末總結與遮住主文自測時，康乃爾版型更適合。 細小格子只宜短語，不適合長篇段落。

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

`python scripts/build.py --ids two-right-narrow`

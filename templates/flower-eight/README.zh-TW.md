# 八瓣想法花

`flower-eight` · `mandala` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![八瓣想法花](previews/a5-draft.png)

用中央圓與八個花瓣泡泡收集主題周圍的短想法。

## 適合情境

- 替故事主角發想八個性格線索。
- 替活動主題蒐集不同的參與方式。

## 使用步驟

1. 中央寫一個主題。
2. 每瓣先填一個短詞，避免在第一輪重複。
3. 回看相鄰花瓣，圈出值得組合的想法。

## 整理後可得到

從中心主題展開多個可再追問的面向。


## 實際填寫示例

示例圍繞虛構社區花園，填入種植、休息、學習、分享、維護、工具、雨水與步道。

![八瓣想法花 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

瓣形重疊不代表集合交集；需要精確分類時改用九宮或表格。

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

`python scripts/build.py --ids flower-eight`

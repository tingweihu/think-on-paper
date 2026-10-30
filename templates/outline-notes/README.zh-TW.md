# 縮排綱要筆記

`outline-notes` · `learning` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![縮排綱要筆記](previews/a5-draft.png)

用縮排顯示主題、子題與例子的三層關係。

## 適合情境

- 整理講座的三個主要段落與各自細節。
- 在撰寫短文前安排段落骨架。

## 使用步驟

1. 每組第一行寫一個主題。
2. 第二與第三行逐級縮排，只寫屬於上一層的內容。
3. 讀回綱要，若層次混亂就移動或重寫該行。

## 整理後可得到

把概念、線索與回想結果相互對照。


## 實際填寫示例

虛構講座的三個段落是背景、示範、討論；每段下再列一個要點和一個例子。

![縮排綱要筆記 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

縮排不表示時間、因果或重要程度；交叉連結較多時改用網絡。

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

修改 `profiles/a5-draft.json` 或 `src/noteformats/layouts/` 內對應的繪圖函式，再於專案根目錄執行：

`python scripts/build.py --ids outline-notes`

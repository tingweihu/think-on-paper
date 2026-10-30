# 六枝概念圖

`mindmap-six` · `concept-network` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![六枝概念圖](previews/a5-draft.png)

從一個中心主題展開六個不同面向，先看想法的廣度。

## 適合情境

- 為小型展覽收集觀眾、空間與材料等方向時。
- 閱讀一章後，把六個關鍵概念先分開記錄時。

## 使用步驟

1. 中心只寫一個明確主題。
2. 外圍六圈各寫一個不同的面向，不要重複同義詞。
3. 圈出需要深入的面向，另用空白頁補細節。

## 整理後可得到

看見主題、分支及需要再確認的關係。


## 實際填寫示例

以虛構社區展覽為中心，依次寫下觀眾、場地、作品、預算、志工與宣傳，之後先追查場地限制。

![六枝概念圖 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

每個外圈只能容納短詞；需要層層推理或長句時，改用樹狀或分欄版型。

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

`python scripts/build.py --ids mindmap-six`

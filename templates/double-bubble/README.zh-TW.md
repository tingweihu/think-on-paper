# 雙核心氣泡比較

`double-bubble` · `comparison` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![雙核心氣泡比較](previews/a5-draft.png)

兩個中心主題連向共通與各自獨有的短特徵。

## 適合情境

- 比較兩種導覽方式的共通目的與差異。
- 整理兩件物品相同功能與不同用法。

## 使用步驟

1. 在左右大圓寫兩個主題。
2. 在上下共通泡泡寫兩者共有的特徵。
3. 最外側小泡泡寫各自獨有的特徵，再檢查連線是否成立。

## 整理後可得到

用同一組條件逐一比較選項，避免只憑單一印象。


## 實際填寫示例

示例比較紙本與口頭導覽；路線和資訊是共通點，可留存與可提問是各自特色。

![雙核心氣泡比較 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

泡泡小，只能寫短詞；需詳細證據或數量比較時應轉成表格。

## 下載

- [無字 SVG](exports/a5-draft/blank.svg)
- [無字 PDF](exports/a5-draft/blank.pdf)
- [左上角英文名稱 PDF](exports/a5-draft/titled.pdf)
- [深色墨線無字 PDF](exports/a5-contrast/blank.pdf)
- [深色墨線 SVG](exports/a5-contrast/blank.svg)

英文名稱只印在標題版 PDF；無字版仍適合自由列印與改作。

頁面尺寸：A5（148 × 210 mm）；設定檔：`a5-draft`。

## 來源與狀態

既有方法的版面改編 · 詳細來源紀錄見 [manifest.json](manifest.json)  
[MIT 授權範圍](../../LICENSE-SCOPE.md)

[三語術語表](../../docs/zh-TW/glossary.md)

## 修改與重新生成

修改 `profiles/a5-draft.json` 或 `src/noteformats/layouts/` 內對應的繪圖函式，再於專案根目錄執行：

`python scripts/build.py --ids double-bubble`

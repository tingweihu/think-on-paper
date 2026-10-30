# 階梯式層級筆記

`stepped-hierarchy` · `hierarchy` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![階梯式層級筆記](previews/a5-draft.png)

把抽象想法逐階轉成更具體、可執行的層次。

## 適合情境

- 將活動宗旨逐步寫成工作項目。
- 讀完論述後，從大主張走向例子與檢查。

## 使用步驟

1. 第一階寫總目標。
2. 每下一階只增加一層具體性，保留與上一階的對應。
3. 最後一階寫可觀察的下一步，檢查是否真由前面推得。

## 整理後可得到

區分上位目標與下位要素，檢查是否遺漏。


## 實際填寫示例

虛構讀書會從『交流閱讀』走到『每月聚會』『輪流提問』『先約場地』。

![階梯式層級筆記 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

階梯容易暗示必然先後；多條並行分支應改用樹或欄。

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

`python scripts/build.py --ids stepped-hierarchy`

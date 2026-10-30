# 七張發想卡

`seven-ideation-cards` · `ideation` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![七張發想卡](previews/a5-draft.png)

將多個候選想法放進各自的獨立卡片，再比較或排序。 本款的幾何變化： 獨立卡片數: 7.

## 適合情境

**幾何對照:** `parameter` · [four-cards](../four-cards/README.zh-TW.md)

- 為一個展覽主題收集七個獨立構想，每卡保留一項可延伸的提案。
- 列七種活動開場方式，再選兩種做進一步草擬。

## 使用步驟

1. 先決定各卡是不同方案還是同一主題的不同面向，每張只放一個可比較單位。
2. 參考本頁示例，各區依序記錄：1「展板」；2「音訊」；3「導覽」；4「書桌」；5「路線」；6「問答」；7「共讀」
3. 回看各區，標記仍待查證的內容，再決定下一步。

## 整理後可得到

保留多種方案並說明下一輪篩選依據。


## 實際填寫示例

依圖中填寫位置順序列出，每個編號是一筆示例條目：

1. 展板
2. 音訊
3. 導覽
4. 書桌
5. 路線
6. 問答
7. 共讀

![七張發想卡 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

七張卡只是收集提案的容量，不是構想品質或完整性的門檻；篩選時仍須另訂條件，不宜用卡片位置當作排名。

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

`python scripts/build.py --ids seven-ideation-cards`

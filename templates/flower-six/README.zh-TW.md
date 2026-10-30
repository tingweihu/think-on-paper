# 六瓣發想花

`flower-six` · `mandala` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![六瓣發想花](previews/a5-draft.png)

從中心主題向周圍六個泡泡延伸不同想法。 本款的幾何變化： 中心外圈數: 6.

## 適合情境

**幾何對照:** `parameter` · [flower-eight](../flower-eight/README.zh-TW.md)

- 圍繞一個故事人物，用六個花瓣分別探索動機、習慣或背景面向。
- 以社區活動為中心，分出六個互不重複的參與需求。

## 使用步驟

1. 中央寫主題，外圈每個圓放一個不同面向，避免重複詞。
2. 參考本頁示例，各區依序記錄：1「社區花園」；2「種植」；3「休息」；4「學習」；5「分享」；6「維護」；7「工具」
3. 回看各區，標記仍待查證的內容，再決定下一步。

## 整理後可得到

從中心主題展開多個可再追問的面向。


## 實際填寫示例

依圖中填寫位置順序列出，每個編號是一筆示例條目：

1. 社區花園
2. 種植
3. 休息
4. 學習
5. 分享
6. 維護
7. 工具

![六瓣發想花 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

六個花瓣用來展開面向，重疊外形不表示集合交集或因果；需要明確分類規則與隸屬關係時，應改用矩陣或概念網絡。

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

調整 `src/noteformats/variants.py` 的幾何或 `src/noteformats/variant_content.py` 的文字，再於專案根目錄執行：

`python scripts/build.py --ids flower-six`

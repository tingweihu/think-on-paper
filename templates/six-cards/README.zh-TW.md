# 六張獨立卡

`six-cards` · `cards` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![六張獨立卡](previews/a5-draft.png)

將多個候選想法放進各自的獨立卡片，再比較或排序。 本款的幾何變化： 獨立卡片數: 6.

## 適合情境

**幾何對照:** `parameter` · [four-cards](../four-cards/README.zh-TW.md)

- 為六位受訪者各留一張摘要卡，方便回看共同點。
- 讀完章節後整理六項概念，每格放一項定義與短例。

## 使用步驟

1. 先決定各卡是不同方案還是同一主題的不同面向，每張只放一個可比較單位。
2. 參考本頁示例，各區依序記錄：1「圖書館十席」；2「四本短篇」；3「週五前通知」；4「週六下午」；5「兩人引導」；6「收回饋卡」
3. 回看各區，標記仍待查證的內容，再決定下一步。

## 整理後可得到

把可移動的事項分開，方便排序、比較或選擇。


## 實際填寫示例

依圖中填寫位置順序列出，每個編號是一筆示例條目：

1. 圖書館十席
2. 四本短篇
3. 週五前通知
4. 週六下午
5. 兩人引導
6. 收回饋卡

![六張獨立卡 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

六卡可各放一項摘要，但彼此位置不表示時間順序或因果；完整訪談逐字稿與跨卡關係需要另外記錄。

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

`python scripts/build.py --ids six-cards`

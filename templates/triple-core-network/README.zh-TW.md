# 三核心關係網

`triple-core-network` · `concept-network` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![三核心關係網](previews/a5-draft.png)

同時檢視三個互相影響的核心因素及各自的外部條件。

## 適合情境

- 討論小型活動的內容、人力與空間如何互相牽動。
- 規劃課程時比較目標、時間與材料的依賴。

## 使用步驟

1. 中間三圈各寫一個核心因素。
2. 外側填入具體條件，連到最相關的核心。
3. 逐條檢查三角內的關係是否有事實支持。

## 整理後可得到

看見主題、分支及需要再確認的關係。


## 實際填寫示例

虛構讀書活動以內容、志工、空間為核心，外側記主題、主持、座位、時段及材料。

![三核心關係網 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

連線是待查假設，不表示三因素一定有因果；外圈也不夠寫長證據。

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

`python scripts/build.py --ids triple-core-network`

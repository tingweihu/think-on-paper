# 觀察與解釋

`observation-interpretation` · `research` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![觀察與解釋](previews/a5-draft.png)

一欄記直接觀察，另一欄記暫時解釋，避免混為事實。

## 適合情境

**幾何對照:** `equivalent` · [two-equal-columns](../two-equal-columns/README.zh-TW.md)

- 觀察工作坊互動時，把可見行為與自己猜測的理由分欄記錄。
- 檢視物件使用情形，左列寫實際看到的現象，右列寫待查解釋。

## 使用步驟

1. 左欄只記看到或聽到的具體現象，不寫原因猜測。
2. 右欄寫可能解釋，並以記號連回對應觀察。
3. 檢查每項解釋還需要哪些資料，保留其他可能的解讀。

## 整理後可得到

分開來源、引文、主張與待查問題。


## 實際填寫示例

依圖中填寫位置順序列出，每個編號是一筆示例條目：

1. 觀察：三人遲到
2. 解釋：或與時段有關；應詢問

![觀察與解釋 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

可見行為不能直接證明他人的動機；觀察者的選擇與視角也會影響記錄，解釋欄應保留其他可能與待查資料。

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

`python scripts/build.py --ids observation-interpretation`

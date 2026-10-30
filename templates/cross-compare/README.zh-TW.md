# 交叉比較四區

`cross-compare` · `comparison` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![交叉比較四區](previews/a5-draft.png)

以兩個選定標準把四個方案分入交叉區域，比較取捨。

## 適合情境

**幾何對照:** `equivalent` · [quadrant](../quadrant/README.zh-TW.md)

- 用成本與可逆性兩個標準，把四個活動方案放進交叉區比較。
- 將四項改善提案依準備時間與影響範圍分類，討論先試哪一項。

## 使用步驟

1. 以兩個選定標準把四個方案分入交叉區域，比較取捨。
2. 每個想法寫成短句，放入最接近的區域。
3. 不確定的想法先放在邊界，並記下需要查證的條件。
4. 比較各區密度，選出下一步要試做或調查的項目。

## 整理後可得到

用同一組條件逐一比較選項，避免只憑單一印象。


## 實際填寫示例

依圖中填寫位置順序列出，每個編號是一筆示例條目：

1. 提問：高價值低投入
2. 告示：低價值低投入
3. 互動練習：高價值高投入
4. 長講義：低價值高投入

![交叉比較四區 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

互相依賴很多的條件或需要精確權重的決策，不宜只靠四區分類。 細小格子只宜短語，不適合長篇段落。

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

`python scripts/build.py --ids cross-compare`

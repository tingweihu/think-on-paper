# 四象限筆記

`quadrant` · `matrix` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![四象限筆記](previews/a5-draft.png)

用兩個自訂面向把想法分成四區，觀察分布與缺口。

## 適合情境

- 準備工作坊時，用參與價值與準備投入比較活動構想。
- 讀書時，用主題與證據強度整理不同段落。

## 使用步驟

1. 先選兩個不同的比較面向，在紙上自行註明四區的意思。
2. 每個想法寫成短句，放入最接近的區域。
3. 不確定的想法先放在邊界，並記下需要查證的條件。
4. 比較各區密度，選出下一步要試做或調查的項目。

## 整理後可得到

看見兩個以上維度交叉處的資料缺口與取捨。


## 實際填寫示例

虛構的小型工作坊規劃：把現場示範、完整互動教材、提問時間與長篇講義依參與價值和準備投入暫時分區。

![四象限筆記 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

互相依賴很多的條件或需要精確權重的決策，不宜只靠四區分類。

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

`python scripts/build.py --ids quadrant`

# 引文與旁註

`quote-side-notes` · `research` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![引文與旁註](previews/a5-draft.png)

寬欄保留短引文，窄欄記來源或待查問題。

## 適合情境

**幾何對照:** `equivalent` · [two-left-narrow](../two-left-narrow/README.zh-TW.md)

- 在大欄摘錄一段文章，左側窄欄補來源頁碼與詞義註記。
- 保留虛構海報的文字內容，將日期或措辭疑問寫在旁欄。

## 使用步驟

1. 寬欄保留短引文，窄欄記來源或待查問題。
2. 在右欄記錄主要內容，對應左欄的索引保持相近高度。
3. 回顧時以左欄快速定位，確認右欄仍有足夠脈絡。

## 整理後可得到

分開來源、引文、主張與待查問題。


## 實際填寫示例

依圖中填寫位置順序列出，每個編號是一筆示例條目：

1. 待核：日期
2. 虛構海報：『週六下午開放』。

![引文與旁註 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

旁欄只容納精簡註記，不能取代完整的上下文與來源記錄；截取短句時要回查前後文，避免改變原意。

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

`python scripts/build.py --ids quote-side-notes`

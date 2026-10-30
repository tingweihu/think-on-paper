# 三格故事板

`storyboard-three` · `storyboard` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![三格故事板](previews/a5-draft.png)

用連續畫格描繪同一事件的變化，並在每格留下動作提示。 本款的幾何變化： 故事板畫格數: 3.

## 適合情境

**幾何對照:** `parameter` · [storyboard-6](../storyboard-6/README.zh-TW.md)

- 用三格呈現短片的開場、轉折與結尾，先確認故事是否連得起來。
- 將服務體驗壓縮為到達、操作、離開三個關鍵場景。

## 使用步驟

1. 先把事件分成與本頁畫格數相符的關鍵場景，每格畫出可見的變化。
2. 參考本頁示例，各區依序記錄：1「入館」；2「找書」；3「討論」
3. 回看各區，標記仍待查證的內容，再決定下一步。

## 整理後可得到

從連續畫面看出事件轉折與仍缺的鏡頭。


## 實際填寫示例

依圖中填寫位置順序列出，每個編號是一筆示例條目：

1. 入館
2. 找書
3. 討論

![三格故事板 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

三格只能保留少量關鍵轉折；需要呈現細部動作、鏡頭銜接或精確時長的故事，應增加畫格與拍攝註記。

## 下載

- [無字 SVG](exports/a5-draft/blank.svg)
- [無字 PDF](exports/a5-draft/blank.pdf)
- [左上角英文名稱 PDF](exports/a5-draft/titled.pdf)
- [深色墨線無字 PDF](exports/a5-contrast/blank.pdf)
- [深色墨線 SVG](exports/a5-contrast/blank.svg)

英文名稱只印在標題版 PDF；無字版仍適合自由列印與改作。

頁面尺寸：A5（148 × 210 mm）；設定檔：`a5-draft`。

## 來源與狀態

傳統格式改編 · 詳細來源紀錄見 [manifest.json](manifest.json)  
[MIT 授權範圍](../../LICENSE-SCOPE.md)

[三語術語表](../../docs/zh-TW/glossary.md)

## 修改與重新生成

調整 `src/noteformats/variants.py` 的幾何或 `src/noteformats/variant_content.py` 的文字，再於專案根目錄執行：

`python scripts/build.py --ids storyboard-three`

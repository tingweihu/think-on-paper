# 四格故事板

`storyboard-four` · `storyboard` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [返回目錄](../../docs/zh-TW/catalog.md)

![四格故事板](previews/a5-draft.png)

用連續畫格描繪同一事件的變化，並在每格留下動作提示。 本款的幾何變化： 故事板畫格數: 4.

## 適合情境

**幾何對照:** `parameter` · [storyboard-6](../storyboard-6/README.zh-TW.md)

- 以四格畫出人物遇到問題、嘗試、獲得回饋與調整的過程。
- 把一段操作教學拆成四個能看出變化的畫面。

## 使用步驟

1. 先把事件分成與本頁畫格數相符的關鍵場景，每格畫出可見的變化。
2. 參考本頁示例，各區依序記錄：1「入館」；2「找書」；3「閱讀」；4「討論」
3. 回看各區，標記仍待查證的內容，再決定下一步。

## 整理後可得到

從連續畫面看出事件轉折與仍缺的鏡頭。


## 實際填寫示例

依圖中填寫位置順序列出，每個編號是一筆示例條目：

1. 入館
2. 找書
3. 閱讀
4. 討論

![四格故事板 填寫示例](examples/zh-TW.svg)

[SVG](examples/zh-TW.svg)

## 不適合情境

四格便於檢查短事件的起承轉合，但不能完整記錄多條支線；每格包含幾個鏡頭或多久時間，也須另外註明。

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

`python scripts/build.py --ids storyboard-four`

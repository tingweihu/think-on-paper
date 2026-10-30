# 第三方依賴與素材

本專案未捆綁下表的外部工具或字型檔。原創內容採 [MIT](LICENSE)；第三方工具與字型仍適用各自的條件，若日後捆綁或再散布，須核對該版本的正式條款與公告要求。

| 項目 | 本專案用途 | 本地證據 | 若日後捆綁或再散布的工作 |
|---|---|---|---|
| Pillow 12.1.1 | PNG 預覽合成與驗證 | `requirements.txt` | 若捆綁套件，核對該版本正式授權與公告要求；目前只列為安裝依賴 |
| pypdf 6.7.5 | PDF 結構檢查 | `requirements.txt` | 若捆綁套件，核對該版本正式授權與公告要求；目前只列為安裝依賴 |
| Poppler `pdftoppm` | 將對應 PDF 渲染為 PNG | `scripts/build.py`、`scripts/qa.py` | 核對版本、取得方式及若隨包提供時的再散布條件；目前不捆綁 |
| Python 3.12 | 程式執行環境 | 文件與腳本 | 記錄目標版本與取得方式；不隨包提供執行環境 |
| `Arial, sans-serif` | 示例 SVG 的檢視器字型選擇 | `src/noteformats/exporters.py`、`examples.py` | 本專案未捆綁字型；確認目標檢視器的替代字型、顯示與任何未來嵌入字型的授權 |
| PDF Standard 14 `Helvetica` | `titled.pdf` 左上角英文版型名 | `src/noteformats/exporters.py` | PDF 僅引用標準字型名稱，未捆綁字型檔；不同檢視器可能選用替代字型 |
| 外部圖片／圖示／音訊／影片／字型檔 | 本地逐檔盤點未檢出捆綁檔案，720 份 SVG 也未檢出外部素材引用 | [`docs/SOURCES-AND-RIGHTS.md`](docs/SOURCES-AND-RIGHTS.md) | 未來新增外部素材時須先確認來源、權利和是否可隨 MIT 專案散布 |

版型 Manifest 的 `source_type`、`source_note` 與 `content/merged.json` 提供方法與幾何來源線索，但不能證明沒有外部作品相似性。25 款具名方法或紙張的檢查清單在 [`docs/SOURCES-AND-RIGHTS.md`](docs/SOURCES-AND-RIGHTS.md)；不宣稱獨占通用方法或商業模板。

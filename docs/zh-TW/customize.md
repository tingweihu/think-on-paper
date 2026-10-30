# 修改與重新生成

[返回首頁](../../README.md) · [English](../en/customize.md) · [日本語](../ja/customize.md)

紙張尺寸、邊界、線寬、墨色與預覽紙色集中在 [`profiles/a5-draft.json`](../../profiles/a5-draft.json)。幾何原語在 [`src/noteformats/geometry.py`](../../src/noteformats/geometry.py)，基本版型的構圖函式在 `src/noteformats/layouts/`，參數變體在 `src/noteformats/variants.py`。示例文字在 `content/` 與 `src/noteformats/variant_content.py`，不會進入空白紙。

建置環境需有 Python 3.12、[`requirements.txt`](../../requirements.txt) 中的 Pillow 與 pypdf，以及 PATH 中的 Poppler `pdftoppm`。本次驗證使用 Python 3.12.10、Pillow 12.1.1、pypdf 6.7.5、Poppler 26.07.0。依賴已備妥後，生成與 QA 不需要網路。

從專案根目錄執行：

```powershell
python scripts/build.py --ids quadrant
python -B scripts/generate_docs.py
python scripts/qa.py
```

生成器也會輸出 `titled.pdf`，左上角有英文版型名稱。原有 `blank.pdf` 與 SVG 保持無字；PNG 仍由無字 PDF 渲染。QA 逐款檢查名稱文字與 PDF 頁面。

第一行重新生成該款空白 SVG、PDF、由 PDF 渲染的 PNG 和三語示例；最後一行核查尺寸、空白、內容與路徑。需要更多版型時省略 `--ids`，但不要手改 `templates/*/exports/` 內可再生檔案。

## Windows、macOS、Linux 建置

可把專案複製到任意目錄，並從該目錄的根目錄執行命令。生成器依腳本位置辨識專案。需預先備妥 Python 3.12、已鎖定的 Python 套件及 Poppler `pdftoppm`。

- Windows PowerShell：`python -B scripts/build.py`，接著 `python -B scripts/generate_docs.py` 與 `python -B scripts/qa.py`。
- macOS／Linux shell：`python3 -B scripts/build.py`，接著 `python3 -B scripts/generate_docs.py` 與 `python3 -B scripts/qa.py`。

生成器拒絕連結、路徑穿越和工作副本外的輸出路徑。

[Build and verify](../BUILD-AND-VERIFY.md)

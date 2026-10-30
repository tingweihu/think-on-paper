# 変更と再生成

[ホーム](../../README.ja.md) · [繁體中文](../zh-TW/customize.md) · [English](../en/customize.md)

用紙寸法、余白、線幅、インク色、プレビューの紙色は [`profiles/a5-draft.json`](../../profiles/a5-draft.json) にまとまっています。共通の図形は [`src/noteformats/geometry.py`](../../src/noteformats/geometry.py)、基本の構図は `src/noteformats/layouts/`、派生形は `src/noteformats/variants.py` にあります。記入例の文章は `content/` と `src/noteformats/variant_content.py` にあり、空白版には入りません。

生成には Python 3.12、[`requirements.txt`](../../requirements.txt) の Pillow と pypdf、PATH 上の Poppler `pdftoppm` が必要です。今回の検証環境は Python 3.12.10、Pillow 12.1.1、pypdf 6.7.5、Poppler 26.07.0 です。依存ツールを用意した後の生成と QA にはネットワークが不要です。

プロジェクトのルートで実行します。

```powershell
python scripts/build.py --ids quadrant
python -B scripts/generate_docs.py
python scripts/qa.py
```

生成器は左上に英語の形式名を入れた `titled.pdf` も出力します。既存の `blank.pdf` と SVG は文字のないままで、PNG は空白 PDF から作成します。QA は各形式の名称と PDF ページを検査します。

最初のコマンドは空白SVG/PDF、PDFから作るPNG、三言語の例を再生成します。最後のコマンドは寸法、無字、内容とリンクを検査します。実装済みの全形式を作るときは `--ids` を省きます。`templates/*/exports/` は再生成可能な出力として扱ってください。

## Windows・macOS・Linux での生成

任意の場所にチェックアウトし、そのルートから実行できます。生成器はスクリプトの位置からプロジェクトを認識します。Python 3.12、指定された Python パッケージ、Poppler の `pdftoppm` を事前に用意してください。

- Windows PowerShell: `python -B scripts/build.py`、続いて `python -B scripts/generate_docs.py` と `python -B scripts/qa.py`。
- macOS／Linux shell: `python3 -B scripts/build.py`、続いて `python3 -B scripts/generate_docs.py` と `python3 -B scripts/qa.py`。

生成器はリンク、パスの遡り、チェックアウト外への出力を拒否します。

[Build and verify](../BUILD-AND-VERIFY.md)

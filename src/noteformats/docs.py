from __future__ import annotations

from html import escape

LANGS = ("zh-TW", "en", "ja")
DOC_NAMES = {"zh-TW": "README.zh-TW.md", "en": "README.en.md", "ja": "README.ja.md"}
LABELS = {
    "zh-TW": {"when": "適合情境", "steps": "使用步驟", "example": "實際填寫示例", "unsuitable": "不適合情境", "downloads": "下載", "source": "來源與狀態", "edit": "修改與重新生成", "profile": "頁面尺寸：A5（148 × 210 mm）；設定檔：`a5-draft`。", "back": "返回目錄", "example_alt": "填寫示例", "record": "詳細來源紀錄見", "edit_help": "修改 `profiles/a5-draft.json` 或 `src/noteformats/layouts/` 內對應的繪圖函式，再於專案根目錄執行："},
    "en": {"when": "When to use it", "steps": "How to use it", "example": "Worked example", "unsuitable": "When not to use it", "downloads": "Downloads", "source": "Provenance and status", "edit": "Modify and rebuild", "profile": "Page size: A5 (148 × 210 mm); profile: `a5-draft`.", "back": "Back to catalog", "example_alt": "worked example", "record": "Detailed source record:", "edit_help": "Change `profiles/a5-draft.json` or the corresponding builder in `src/noteformats/layouts/`, then run from the project root:"},
    "ja": {"when": "向いている場面", "steps": "使い方", "example": "記入例", "unsuitable": "向いていない場面", "downloads": "ダウンロード", "source": "由来と状態", "edit": "変更と再生成", "profile": "用紙サイズ：A5（148 × 210 mm）。設定ファイル：`a5-draft`。", "back": "一覧へ戻る", "example_alt": "記入例", "record": "詳しい由来の記録：", "edit_help": "`profiles/a5-draft.json` または `src/noteformats/layouts/` の描画関数を変更し、プロジェクトのルートで実行します："},
}

RESULT_LABEL = {"zh-TW": "整理後可得到", "en": "What the page helps you see", "ja": "記入後に見えること"}
RESULT_BY_FAMILY = {
    "foundation": ("留下可循序回看的筆記或草稿，標出仍待確認的部分。", "A continuous note or draft that can be revisited, with unresolved points marked.", "読み返せる連続した記録や下書きと、未確認の点が残ります。"),
    "grid-dot": ("用格線或點位對齊物件、數量與相對位置。", "Aligned objects, counts, or spatial positions on the grid or dots.", "方眼や点に沿って物、数、位置をそろえられます。"),
    "geometry": ("看出方向、比例或空間配置中需要再測量之處。", "A draft of direction, proportion, or placement, with measurements still to check.", "向き、比率、配置と、追加で測る箇所が見えます。"),
    "columns": ("對照分欄內容，找出相同點、差異與待查證資訊。", "Parallel notes whose agreements, differences, and unanswered points can be checked.", "並べた記録から共通点、相違点、未確認事項を確かめられます。"),
    "cards": ("把可移動的事項分開，方便排序、比較或選擇。", "Separate units that can be reordered, compared, or selected.", "項目を分けて、並べ替えや比較、選択ができます。"),
    "comparison": ("用同一組條件逐一比較選項，避免只憑單一印象。", "Options compared against shared criteria rather than one impression.", "同じ条件で選択肢を見比べ、一つの印象だけで決めることを避けられます。"),
    "matrix": ("看見兩個以上維度交叉處的資料缺口與取捨。", "Intersections, missing cells, and tradeoffs across chosen dimensions.", "複数の観点が交わる場所と、空白や選択上の差が見えます。"),
    "mandala": ("從中心主題展開多個可再追問的面向。", "Several directions to explore from a central topic.", "中心のテーマから次に調べる方向を広げられます。"),
    "concept-network": ("看見主題、分支及需要再確認的關係。", "A map of topics, branches, and relationships still to verify.", "主題と枝、確かめ直す関係を一覧できます。"),
    "hierarchy": ("區分上位目標與下位要素，檢查是否遺漏。", "Levels of a goal or topic, with gaps easier to notice.", "目的や話題の階層と、抜けている要素が見えます。"),
    "flow": ("沿箭頭追查步驟、分岔或循環的先後關係。", "A sequence, branch, or loop that can be traced along its arrows.", "矢印に沿って順序、分岐、循環を追えます。"),
    "causal": ("分開觀察結果與原因假設，標出尚無證據的連結。", "Observed outcomes separated from causal hypotheses and unsupported links.", "観察結果と原因の仮説を分け、根拠のない関係を示せます。"),
    "learning": ("把概念、線索與回想結果相互對照。", "Concepts, cues, and recalled answers that can be checked against one another.", "概念、手がかり、思い出した答えを照合できます。"),
    "research": ("分開來源、引文、主張與待查問題。", "Sources, quotations, claims, and open checks kept distinct.", "資料、引用、主張、未確認事項を分けられます。"),
    "ideation": ("保留多種方案並說明下一輪篩選依據。", "Multiple proposals with a basis for the next selection step.", "複数の案と、次に選ぶための基準が残ります。"),
    "storyboard": ("從連續畫面看出事件轉折與仍缺的鏡頭。", "A visual sequence showing transitions and missing shots.", "連続した場面から変化や足りないカットが見えます。"),
    "special-paper": ("依專用線格留下可檢查的記譜、練字或草圖。", "Notation, letterforms, or sketches aligned to the specialized guides.", "専用の罫線に沿った記譜、文字、下書きを確認できます。"),
    "hybrid": ("把圖、短記與結論放在各自區域，再檢查關係。", "A drawing, short notes, and a conclusion kept separate but connected.", "図、短い記録、結論を分けながら関係づけられます。"),
}

RESULT_BY_ID = {
    "cornell": (
        "利用提示欄遮住主筆記自我回想，再用頁末摘要檢查理解與待補之處。",
        "Use the cue column to recall with the main notes covered, then check understanding and open questions in the bottom summary.",
        "手がかり欄を見て本文を隠したまま思い出し、下の要約で理解と未確認点を確かめられます。",
    ),
    "cornell-mirrored": (
        "用右側提示欄回想左側主筆記，再用頁末摘要核對理解與疑問。",
        "Recall the main notes from the right-hand cues, then use the bottom summary to check understanding and questions.",
        "右の手がかり欄から左の本文を思い出し、下の要約で理解と疑問を確認できます。",
    ),
    "recall-strip": (
        "把回想結果寫進獨立區域，對照原筆記檢查哪些重點仍記不清。",
        "Record recall in a separate strip, then compare it with the notes to see which points remain unclear.",
        "想起した内容を別の帯に書き、元のノートと比べて曖昧な点を確かめられます。",
    ),
}


def result_text(layout_id: str, family: str, lang: str) -> str:
    return RESULT_BY_ID.get(layout_id, RESULT_BY_FAMILY[family])[LANGS.index(lang)]

SOURCE_LABEL = {
    "zh-TW": {"original-layout": "本專案原創版面", "original-hybrid": "本專案原創混合版面", "common-geometry": "通用幾何結構", "generic-geometry": "通用幾何結構", "existing-method-adaptation": "既有方法的版面改編", "traditional-format-adaptation": "傳統格式改編", "traditional-paper": "傳統書寫紙改編", "traditional-paper-adaptation": "傳統書寫紙改編"},
    "en": {"original-layout": "Original layout", "original-hybrid": "Original mixed layout", "common-geometry": "Common geometry", "generic-geometry": "Generic geometry", "existing-method-adaptation": "Adaptation of an existing method", "traditional-format-adaptation": "Adaptation of a traditional format", "traditional-paper": "Adaptation of traditional writing paper", "traditional-paper-adaptation": "Adaptation of traditional writing paper"},
    "ja": {"original-layout": "本プロジェクトの独自レイアウト", "original-hybrid": "本プロジェクトの独自の複合配置", "common-geometry": "一般的な幾何構造", "generic-geometry": "一般的な幾何構造", "existing-method-adaptation": "既存の方法を配置に応用", "traditional-format-adaptation": "伝統的な形式の応用", "traditional-paper": "伝統的な練習紙の応用", "traditional-paper-adaptation": "伝統的な練習紙の応用"},
}


def template_doc(layout_id: str, family: str, item: dict, lang: str) -> str:
    t, l = item["translations"][lang], LABELS[lang]
    edit_help = l["edit_help"]
    if "variant_of" in item and layout_id not in ("t-comparison", "three-way-comparison"):
        edit_help = {
            "zh-TW": "調整 `src/noteformats/variants.py` 的幾何或 `src/noteformats/variant_content.py` 的文字，再於專案根目錄執行：",
            "en": "Edit geometry in `src/noteformats/variants.py` or text in `src/noteformats/variant_content.py`, then run from the project root:",
            "ja": "図形は `src/noteformats/variants.py`、文章は `src/noteformats/variant_content.py` を変更し、プロジェクトのルートで実行します：",
        }[lang]
    lines = [
        f"# {t['title']}", "",
        f"`{layout_id}` · `{family}` · `a5-draft`", "",
        f"[繁體中文]({DOC_NAMES['zh-TW']}) · [English]({DOC_NAMES['en']}) · [日本語]({DOC_NAMES['ja']}) · [{l['back']}](../../docs/{lang}/catalog.md)", "",
        f"![{t['title']}](previews/a5-draft.png)", "",
        t["purpose"], "",
        f"## {l['when']}", "",
    ]
    if "variant_of" in item:
        variant_label = {
            "zh-TW": "幾何對照", "en": "Geometry relationship", "ja": "図形の対応",
        }[lang]
        target = item["variant_of"]
        lines.extend([f"**{variant_label}:** `{item['variant_classification']}` · [{target}](../{target}/{DOC_NAMES[lang]})", ""])
    lines.extend(f"- {x}" for x in t["when"])
    lines.extend(["", f"## {l['steps']}", ""])
    lines.extend(f"{i}. {x}" for i, x in enumerate(t["steps"], 1))
    lines.extend([
        "", f"## {RESULT_LABEL[lang]}", "", result_text(layout_id, family, lang), "",
        "", f"## {l['example']}", "", t["example"], "",
        f"![{t['title']} {l['example_alt']}](examples/{lang}.svg)", "",
        f"[SVG](examples/{lang}.svg)", "",
        f"## {l['unsuitable']}", "", t["unsuitable"], "",
        f"## {l['downloads']}", "",
        f"- [{('無字 SVG', 'Wordless SVG', '文字なしSVG')[LANGS.index(lang)]}](exports/a5-draft/blank.svg)",
        f"- [{('無字 PDF', 'Wordless PDF', '文字なしPDF')[LANGS.index(lang)]}](exports/a5-draft/blank.pdf)",
        f"- [{('左上角英文名稱 PDF', 'PDF with English name at top left', '左上に英語名があるPDF')[LANGS.index(lang)]}](exports/a5-draft/titled.pdf)",
        f"- [{('深色墨線無字 PDF', 'Darker-ink wordless PDF', '濃い線の文字なしPDF')[LANGS.index(lang)]}](exports/a5-contrast/blank.pdf)",
        f"- [{('深色墨線 SVG', 'Darker-ink SVG', '濃い線のSVG')[LANGS.index(lang)]}](exports/a5-contrast/blank.svg)",
        "", ("英文名稱只印在標題版 PDF；無字版仍適合自由列印與改作。", "The English name appears only on the titled PDF; the wordless version remains available for free writing.", "英語名は表題付きPDFだけに印刷され、文字なし版は自由な記入に使えます。")[LANGS.index(lang)], "", l["profile"], "",
        f"## {l['source']}", "",
        f"{SOURCE_LABEL[lang][item['source_type']]} · {l['record']} [manifest.json](manifest.json)  ",
        f"[{('MIT 授權範圍', 'MIT license scope', 'MITライセンスの範囲')[LANGS.index(lang)]}](../../LICENSE-SCOPE.md)", "",
        f"[{('三語術語表', 'Trilingual glossary', '三言語の用語集')[LANGS.index(lang)]}](../../docs/{lang}/glossary.md)", "",
        f"## {l['edit']}", "",
        edit_help, "",
        f"`python scripts/build.py --ids {layout_id}`", "",
    ])
    return "\n".join(lines)


FAMILY_TITLES = {
    "foundation": ("基本書寫", "Basic writing", "基本の書き方"),
    "grid-dot": ("方格與點陣", "Grids and dots", "方眼とドット"),
    "geometry": ("幾何底紙", "Geometry paper", "幾何ガイド"),
    "columns": ("分欄", "Columns", "欄分け"),
    "cards": ("卡片", "Cards", "カード"),
    "comparison": ("比較", "Comparison", "比較"),
    "matrix": ("矩陣與象限", "Matrices and quadrants", "行列と象限"),
    "mandala": ("九宮與花形", "Mandala and flower", "九宮と花形"),
    "concept-network": ("概念網絡", "Concept networks", "概念のネットワーク"),
    "hierarchy": ("層級", "Hierarchy", "階層"),
    "flow": ("流程", "Flows", "流れ図"),
    "causal": ("因果假設", "Causal hypotheses", "因果の仮説"),
    "learning": ("學習與回想", "Learning and recall", "学習と想起"),
    "research": ("資料與研究", "Sources and research", "資料と調査"),
    "ideation": ("發想", "Ideation", "発想"),
    "storyboard": ("故事板與草圖", "Storyboards and sketches", "絵コンテと草図"),
    "special-paper": ("專用書寫紙", "Special writing paper", "専用の練習紙"),
    "hybrid": ("混合版面", "Mixed surfaces", "複合レイアウト"),
}

TASK_GROUPS = (
    (("連續記錄", "Record continuously", "続けて記録する"), ("ruled-standard", "dot-standard", "two-equal-columns", "blank")),
    (("展開與分類想法", "Expand and group ideas", "考えを広げ分類する"), ("mindmap-six", "mandala-3x3", "cluster-ring", "classification-wheel")),
    (("比較與選擇", "Compare and choose", "比較して選ぶ"), ("quadrant", "t-comparison", "venn-two", "matrix-2x3", "bipartite-network")),
    (("學習與自我提問", "Study and retrieve", "学び、問い直す"), ("cornell", "question-answer-triples", "concept-text-diagram", "concept-recall")),
    (("閱讀資料與查證", "Read sources and check claims", "資料を読み、確かめる"), ("top-excerpt-bottom-thoughts", "claim-four-evidence", "source-network-notes", "hypothesis-evidence")),
    (("拆解原因與規劃流程", "Examine causes and plan flows", "原因と手順を整理する"), ("fishbone", "causal-network", "flow-four-horizontal", "decision-tree", "swimlane-flow")),
    (("畫場景與方案", "Sketch scenes and options", "場面と案を描く"), ("storyboard-6", "storyboard-eight-mixed", "three-sketch-proposals", "detail-sketch", "perspective-guides")),
    (("專門練寫", "Use special writing paper", "専用の紙で練習する"), ("music-staff", "guitar-tablature", "hanzi-tian", "hanzi-nine", "seyes-ruled")),
    (("圖文合用", "Combine drawing and notes", "図と文章を組み合わせる"), ("dot-and-blank", "mindmap-and-ruled", "mixed-quadrant", "hybrid-multi-zone")),
)


def _lang_index(lang: str) -> int:
    return LANGS.index(lang)


def _root_name(lang: str) -> str:
    return {"zh-TW": "README.md", "en": "README.en.md", "ja": "README.ja.md"}[lang]


def home(lang: str, verified: list[tuple[str, str, dict]], merged_count: int = 0,
         all_formats: list[tuple[str, str, dict]] | None = None, geometry_count: int = 0) -> str:
    idx = _lang_index(lang)
    titles = ("思考與通用的筆記格式", "Thinking & General Note Formats", "思考と汎用のノートフォーマット")
    intros = ("線、格、圖。依用途找版型、看填寫示例，下載無字或附英文名稱的 PDF。", "Lines, grids, and diagrams. Browse by purpose, see worked examples, and download wordless or English-titled PDFs.", "線・グリッド・図。用途から形式を探し、記入例を見て、文字なしPDFか英語名付きPDFをダウンロードできます。")
    counts = (f"144 款可下載格式・{geometry_count} 種幾何。[共用幾何對照](docs/GEOMETRY-GROUPS.md)", f"144 downloadable formats · {geometry_count} distinct geometries. [Shared geometry](docs/GEOMETRY-GROUPS.md)", f"144形式・{geometry_count}種類の図形。[共通の図形](docs/GEOMETRY-GROUPS.md)")
    story = (
        "起因是手帳習慣。AI 時代，靈感跑進輸入框的速度比找筆還快，但我仍喜歡用線、格、圖整理思路。於是把這些工具畫成可列印、可修改的版型：替手帳留個紀念，也讓它繼續上班。",
        "A planner habit started this project. AI catches ideas faster than I can find a pen, but I still like thinking in lines, grids, and diagrams. These printable, editable pages are a souvenir for the planner—and a new job for it.",
        "手帳を使う習慣から生まれました。AI時代、ペンを探すより先に考えが入力欄へ飛び込みます。それでも線や方眼、図で考えるのが好き。印刷・編集できる形にして、手帳に記念写真と次の仕事を用意しました。",
    )
    banner_alt = ("思考與通用的筆記格式 Banner：線、格、圖", "Thinking & General Note Formats banner: lines, grids, and diagrams", "思考と汎用のノートフォーマットのバナー：線・グリッド・図")
    guide_titles = (("依用途選擇", "完整目錄", "列印", "修改", "貢獻", "術語表"), ("Choose by task", "Full catalog", "Print", "Customize", "Contribute", "Glossary"), ("用途から選ぶ", "全フォーマット一覧", "印刷", "変更", "協力", "用語集"))
    lines = [f"# {titles[idx]}", "", f"![{banner_alt[idx]}](docs/assets/banner.svg)", "", "[繁體中文](README.md) · [English](README.en.md) · [日本語](README.ja.md)", "", intros[idx], "", story[idx], "", counts[idx], "", "## " + ("開始使用", "Start here", "使い始める")[idx], ""]
    lines.append(f"- [{('快速開始', 'Quick start', 'はじめに')[idx]}](QUICKSTART.md)")
    for key, title in zip(("choose", "catalog", "print", "customize", "contribute", "glossary"), guide_titles[idx]):
        lines.append(f"- [{title}](docs/{lang}/{key}.md)")
    gallery = verified if all_formats is None else all_formats
    if gallery:
        lines.extend(["", "## " + ("全部版型：依類別展開", "All formats: expand a family", "全形式：分類を開く")[idx], "",
                      ("展開類別瀏覽；點名稱看完整用法與來源，點圖片放大。",
                       "Expand a family to browse. Open a name for instructions and provenance, or an image for a larger view.",
                       "分類を開いて探せます。名前から使い方と由来へ、画像から拡大表示へ進めます。")[idx], ""])
        families = list(dict.fromkeys(family for _, family, _ in gallery))
        for family in families:
            members = [(layout_id, item) for layout_id, row_family, item in gallery if row_family == family]
            lines.extend([f'<details id="family-{family}">', f'<summary><strong>{FAMILY_TITLES[family][idx]}</strong> · {len(members)}</summary>', ""])
            for layout_id, item in members:
                t = item["translations"][lang]
                base = f"templates/{layout_id}"
                title = escape(t["title"], quote=True)
                lines.extend([f"### [{t['title']}]({base}/{DOC_NAMES[lang]}) · `{layout_id}`", "",
                              f'<a href="{base}/previews/a5-draft.png"><img src="{base}/previews/a5-draft.png" width="138" loading="lazy" alt="{title}"></a>', "",
                              t["purpose"], ""])
                example_alt = escape(f"{t['title']} {LABELS[lang]['example_alt']}", quote=True)
                lines.extend([f"**{LABELS[lang]['example']}：** {t['example']}", "",
                              f'<a href="{base}/examples/{lang}.svg"><img src="{base}/examples/{lang}.svg" width="138" loading="lazy" alt="{example_alt}"></a>', ""])
                lines.extend([f"[{('無字 PDF', 'Wordless PDF', '文字なしPDF')[idx]}]({base}/exports/a5-draft/blank.pdf) · "
                              f"[{('英文名稱 PDF', 'English-titled PDF', '英語名付きPDF')[idx]}]({base}/exports/a5-draft/titled.pdf) · "
                              f"[SVG]({base}/exports/a5-draft/blank.svg) · "
                              f"[{('深色 PDF', 'Darker PDF', '濃い線PDF')[idx]}]({base}/exports/a5-contrast/blank.pdf)", ""])
            lines.extend(["</details>", ""])
    lines.extend(["## " + ("檔案與授權", "Files and license", "ファイルとライセンス")[idx], "",
                  ("無字 SVG／PDF 只含幾何；左上角英文名稱僅在標題版 PDF。暖黃用於預覽，列印 PDF 不印滿版底色。",
                   "Wordless SVG/PDF contain only geometry; the English name appears only in the titled PDF. Warm paper color is for previews, not a full-page print fill.",
                   "文字なしSVG/PDFには図形のみを配置し、英語名は表題付きPDFだけに表示します。淡い暖色はプレビュー用で、印刷PDFを全面塗りつぶしません。")[idx], "",
                  f"[{('建置與驗證', 'Build & verify', '生成と検証')[idx]}](docs/BUILD-AND-VERIFY.md) · [MIT](LICENSE) · [{('授權範圍', 'License scope', 'ライセンスの範囲')[idx]}](LICENSE-SCOPE.md) · [{('來源與權利', 'Sources and rights', '由来と権利')[idx]}](docs/SOURCES-AND-RIGHTS.md)", "",
                  f"[{'貢獻指南' if lang == 'zh-TW' else 'Contributing' if lang == 'en' else '協力ガイド'}](CONTRIBUTING.md) · [Security](SECURITY.md) · [Changelog](CHANGELOG.md)", ""])
    return "\n".join(lines)


def catalog_doc(lang: str, verified: list[tuple[str, str, dict]], merged: dict) -> str:
    idx = _lang_index(lang)
    title = ("完整版型目錄", "Full format catalog", "全フォーマット一覧")[idx]
    intro = ("以下僅列出已驗證且檔案存在的基本版型；縮圖取自對應 PDF 的實際渲染。候選幾何變體列在文末。", "Only verified base formats with real files appear below. Each thumbnail comes from the matching PDF render. Merged candidate IDs are listed at the end.", "以下はファイルが存在する検証済みの基本形式です。縮小画像は対応するPDFから描画しました。統合された候補IDは末尾にあります。")[idx]
    back = ("首頁", "Home", "ホーム")[idx]
    lines = [f"# {title}", "", f"[{back}](../../{_root_name(lang)}) · [繁體中文](../zh-TW/catalog.md) · [English](../en/catalog.md) · [日本語](../ja/catalog.md)", "", intro, "", "## " + ("依外觀找", "Browse by appearance", "外観から探す")[idx], ""]
    families = list(dict.fromkeys(family for _, family, _ in verified))
    for family in families:
        lines.append(f"- [{FAMILY_TITLES[family][idx]}](#{family})")
    for family in families:
        lines.extend(["", f"<a id=\"{family}\"></a>", f"## {FAMILY_TITLES[family][idx]}", ""])
        for layout_id, row_family, item in verified:
            if row_family != family:
                continue
            t = item["translations"][lang]
            base = f"../../templates/{layout_id}"
            lines.extend([f"### [{t['title']}]({base}/{DOC_NAMES[lang]}) · `{layout_id}`", "", f"![{t['title']}：{t['purpose']}]({base}/previews/a5-draft.png)", "", t["purpose"], "", f"[{('無字 PDF', 'Wordless PDF', '文字なしPDF')[idx]}]({base}/exports/a5-draft/blank.pdf) · [{('英文名稱 PDF', 'English-titled PDF', '英語名付きPDF')[idx]}]({base}/exports/a5-draft/titled.pdf) · [SVG]({base}/exports/a5-draft/blank.svg) · [{LABELS[lang]['example']}]({base}/examples/{lang}.svg)", ""])
    alias_title = ("合併的候選 ID", "Merged candidate IDs", "統合した候補ID")[idx]
    alias_intro = ("下列 ID 保留各自可下載的 SVG／PDF 與說明；變體關係記在各款 Manifest。", "Each ID below has its own SVG/PDF downloads and guide; the manifest records its variant relationship.", "次のIDには個別のSVG/PDFと説明があり、派生関係は各Manifestに記録しています。")[idx]
    lines.extend([f"## {alias_title}", "", alias_intro, ""])
    by_id = {layout_id: item for layout_id, _, item in verified}
    for alias, info in merged.items():
        target = info["target"]
        if target in by_id:
            t = by_id[target]["translations"][lang]["title"]
            lines.append(f"- [`{alias}`](../../templates/{alias}/{DOC_NAMES[lang]}) · [PDF](../../templates/{alias}/exports/a5-draft/blank.pdf) · [{('英文名稱 PDF', 'English-titled PDF', '英語名付きPDF')[idx]}](../../templates/{alias}/exports/a5-draft/titled.pdf) · [SVG](../../templates/{alias}/exports/a5-draft/blank.svg) · {t}: `{target}`")
    lines.append("")
    return "\n".join(lines)


def choose_doc(lang: str, verified: list[tuple[str, str, dict]]) -> str:
    idx = _lang_index(lang)
    title = ("依用途選擇版型", "Choose by task", "用途から選ぶ")[idx]
    intro = ("先選你要做的事，再打開版型頁看限制、填寫示例與空白下載。每組只是入門建議；完整名稱與外觀見目錄。", "Start with what you need to do, then open a format page for limits, worked examples, and blank downloads. These are starting points; the full catalog has every verified format.", "まず目的を選び、各形式のページで制約、記入例、空白版を確認してください。ここは入口の提案で、全形式は一覧にあります。")[idx]
    back = ("首頁", "Home", "ホーム")[idx]
    caution = ("限制：", "Limit: ", "制約：")[idx]
    by_id = {layout_id: item for layout_id, _, item in verified}
    lines = [f"# {title}", "", f"[{back}](../../{_root_name(lang)}) · [{('完整目錄', 'Full catalog', '全一覧')[idx]}](catalog.md) · [繁體中文](../zh-TW/choose.md) · [English](../en/choose.md) · [日本語](../ja/choose.md)", "", intro, ""]
    for titles, ids in TASK_GROUPS:
        available = [layout_id for layout_id in ids if layout_id in by_id]
        if not available:
            continue
        lines.extend([f"## {titles[idx]}", ""])
        for layout_id in available:
            t = by_id[layout_id]["translations"][lang]
            lines.append(f"- [{t['title']}](../../templates/{layout_id}/{DOC_NAMES[lang]}) — {t['purpose']} {caution}{t['unsuitable']}")
        lines.append("")
    return "\n".join(lines)

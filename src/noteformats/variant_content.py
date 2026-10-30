"""Three-language guidance for stable variant IDs."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

from .geometry import Scene
from .content_format import region_example, inline_entries
from .variants import ORIGINAL_MERGES, VARIANT_METHODS

COMMON = {
    "zh-TW": {
        "title": "可生成版型", "use": "這是可直接下載的候選版型；請先確認每個區域代表什麼，再參照目標版型的方法填寫。",
        "when": ("需要這個明確的格數、方向或書寫用途時。", "希望直接列印對應幾何，而不是在另一款紙上手繪修改時。"),
        "steps": ("確認這張紙的分區、方向和可寫空間。", "為每區填入一項具體而可追溯的內容；必要時參照對應版型的詳細說明。", "依箭頭或分區順序回看內容，標記仍待查證之處。"),
        "unsuitable": "細小格子只宜短語，不適合長篇段落。",
        "example": "示例以虛構資料在對應區域放入短語，示意填寫位置；不是實測或完整研究結論。",
        "extra": "本款的幾何變化：",
    },
    "en": {
        "title": "Reproducible format", "use": "This candidate has its own downloadable geometry. Define each region before filling it, and consult the linked canonical method where useful.",
        "when": ("Use it when this count, direction, or writing behavior matters.", "Use the actual printable geometry instead of redrawing another sheet by hand."),
        "steps": ("Check the regions, direction, and available writing room on this page.", "Put one specific, traceable entry in each region; consult the related format for method detail.", "Read through the arrows or regions and mark what still needs verification."),
        "unsuitable": "Small cells hold short phrases rather than long paragraphs.",
        "example": "The fictional entries indicate where short notes belong; they are neither measured data nor a complete research conclusion.",
        "extra": "Geometry change:",
    },
    "ja": {
        "title": "再生成できる形式", "use": "この候補には対応するダウンロード可能な図形があります。各領域の意味を決め、必要に応じて関連形式の詳しい使い方を参照します。",
        "when": ("このマス数、向き、または書き方が必要なとき。", "別の紙に手で描き足す代わりに、対応する図形を直接印刷したいとき。"),
        "steps": ("領域、方向、書ける広さを確認します。", "各領域に具体的で後から確かめられる内容を書き、必要なら関連形式の説明を参照します。", "矢印や領域の順に読み直し、未確認の点に印を付けます。"),
        "unsuitable": "小さなマスは短い語句向けで、長い文章には向きません。",
        "example": "架空の短い記入で各領域の使い方を示します。実測データや完全な調査結果ではありません。",
        "extra": "図形の変更：",
    },
}


def change_text(operation: str, value, lang: str) -> str:
    descriptions = {
        "copy": ("與對應版型完全相同的無字幾何，另保留此用途名稱。", "The blank geometry is exactly equivalent; this use name remains searchable.", "空白図形は対応形式と同一で、この用途名を検索用に残します。"),
        "mirror_x": ("左右欄位鏡像。", "The left and right zones are mirrored.", "左右の領域を反転しました。"),
        "mirror_y": ("由下往上閱讀的鏡像層級。", "The hierarchy is mirrored for bottom-up reading.", "下から上へ読むよう階層を反転しました。"),
        "engineering_grid": ("每五格有較明顯的主線。", "Every fifth grid line is emphasized.", "五マスごとに主線を強調しました。"),
        "weighted_matrix": ("三欄兩行，欄寬與行高改為不等比例。", "Three columns by two rows with unequal widths and heights.", "三列二行で、列幅と行高を異なる比率にしました。"),
        "diverging_flow": ("一個問題向外分成三個可採取的結果。", "One starting problem branches into three possible actions.", "一つの問題から三つの対応へ枝分かれします。"),
        "root_cause_tree": ("四個原因候選經兩個群組匯向一個觀察結果。", "Four candidate causes converge through two groups on one observed outcome.", "四つの原因候補が二群を経て一つの観察結果に集まります。"),
        "recall_strip": ("在康乃爾分區下方另留一條回想區。", "A separate recall strip is added below the Cornell zones.", "コーネル式の領域の下に想起用の帯を追加しました。"),
        "mixed_storyboard": ("一個大畫面接三個較小的連續畫面。", "One large scene leads to three smaller sequential frames.", "大きな一場面の後に小さな三場面を並べました。"),
        "ruled_sketch_bottom": ("上方橫線、下方空白草圖區。", "Ruled notes sit above an open sketch area.", "上を横罫、下を自由なスケッチ領域にしました。"),
    }
    if operation in descriptions:
        return descriptions[operation][("zh-TW", "en", "ja").index(lang)]
    n = value if not isinstance(value, tuple) else "×".join(str(x) for x in value)
    kind = {
        "ruled": ("橫線行距", "ruled line spacing", "横罫の間隔"),
        "grid": ("方格間距", "grid pitch", "方眼の間隔"),
        "dot": ("點陣間距", "dot pitch", "ドットの間隔"),
        "fishbone": ("每側原因分枝數", "cause branches per side", "片側の原因枝数"),
        "storyboard": ("故事板畫格數", "storyboard frames", "絵コンテのコマ数"),
        "stacked_cards": ("上下卡片數", "stacked cards", "縦のカード数"),
        "card_grid": ("獨立卡片數", "separate cards", "独立カード数"),
        "matrix": ("矩陣的欄乘列", "matrix columns by rows", "行列の列数×行数"),
        "flower": ("中心外圈數", "outer bubbles", "外側の円数"),
        "vertical_flow": ("垂直步驟數", "vertical steps", "縦の段階数"),
        "cycle": ("循環節點數", "cycle nodes", "循環の節点数"),
        "mindmap": ("心智圖分枝數", "mind-map spokes", "マップの枝数"),
        "pyramid": ("金字塔層數", "pyramid levels", "ピラミッドの段数"),
        "center_satellites": ("中心外側變化數", "outer variation cards", "中心の外側カード数"),
        "converging_flow": ("匯入來源數", "converging inputs", "合流する入力数"),
    }[operation][("zh-TW", "en", "ja").index(lang)]
    unit = " mm" if operation in ("ruled", "grid", "dot") else ""
    return f"{kind}: {n}{unit}."


SPECIAL_LABELS = {
    "mirrored-compare-cards": {
        "zh-TW": ["圖書館：免費", "戶外亭：開放", "圖書館：避雨", "戶外亭：易受天候影響"],
        "en": ["Library: free", "Pavilion: open", "Library: dry", "Pavilion: weather risk"],
        "ja": ["図書館：無料", "東屋：開放的", "図書館：雨を避ける", "東屋：天候の影響"],
    },
    "causal-chain": {
        "zh-TW": ["通知晚？", "看到的人少？", "報名偏少？", "到場偏少？"],
        "en": ["Late notice?", "Few see it?", "Few sign up?", "Few attend?"],
        "ja": ["案内が遅い？", "見る人が少ない？", "申込が少ない？", "出席が少ない？"],
    },
    "frayer": {
        "zh-TW": ["水循環", "定義：水的移動", "特徵：往復", "例：降雨", "非例：水管"],
        "en": ["Water cycle", "Meaning: water moves", "Trait: repeats", "Example: rain", "Nonexample: pipe"],
        "ja": ["水循環", "定義：水の移動", "特徴：繰り返す", "例：雨", "非例：水道管"],
    },
    "cue-answer": {
        "zh-TW": ["葉色與光照？", "窗邊葉較深；也須控制澆水量。"],
        "en": ["Light and leaf color?", "Window leaves darker; control watering too."],
        "ja": ["日照と葉色？", "窓辺の葉が濃い。水やりも比べる。"],
    },
    "concept-examples-six": {
        "zh-TW": ["哺乳類", "貓", "犬", "鯨", "蝙蝠", "海豹", "人"],
        "en": ["Mammal", "Cat", "Dog", "Whale", "Bat", "Seal", "Human"],
        "ja": ["哺乳類", "猫", "犬", "鯨", "コウモリ", "アザラシ", "人"],
    },
    "quote-side-notes": {
        "zh-TW": ["待核：日期", "虛構海報：『週六下午開放』。"],
        "en": ["Check date", "Fictional poster: 'Open Saturday afternoon.'"],
        "ja": ["日付を確認", "架空の掲示：『土曜午後に開場』。"],
    },
    "quote-comment-parallel": {
        "zh-TW": ["引文：『週六下午開放』", "評論：日期與來源待確認"],
        "en": ["Quote: 'Open Saturday'", "Note: verify date and source"],
        "ja": ["引用：『土曜午後に開場』", "注記：日付と出典を確認"],
    },
    "observation-interpretation": {
        "zh-TW": ["觀察：三人遲到", "解釋：或與時段有關；應詢問"],
        "en": ["Observed: three late", "Possible reason: time; ask them"],
        "ja": ["観察：三人が遅刻", "解釈：時間が原因か。本人に確認"],
    },
    "source-large-plus-cards": {
        "zh-TW": ["虛構活動海報", "主張：週六開放", "依據：海報文字", "待查：實際日期"],
        "en": ["Fictional event poster", "Claim: open Saturday", "Evidence: poster text", "Check: actual date"],
        "ja": ["架空の催しの掲示", "主張：土曜に開場", "根拠：掲示の文", "確認：実際の日付"],
    },
    "research-index-cards": {
        "zh-TW": ["來源 A：海報", "來源 B：訪談", "來源 C：網站", "待查：日期差異"],
        "en": ["Source A: poster", "Source B: interview", "Source C: web page", "Check: date conflict"],
        "ja": ["資料A：掲示", "資料B：聞き取り", "資料C：サイト", "確認：日付の差"],
    },
    "pixel-stitch-grid": {
        "zh-TW": ["藍色四格", "白色留空", "待查：線材數"],
        "en": ["Four blue cells", "Leave white gaps", "Check yarn count"],
        "ja": ["青の四マス", "白を空ける", "糸の量を確認"],
    },
    "three-stacked-cards": {
        "zh-TW": ["入口：清楚指引", "活動中：找到書", "活動後：整理回饋"],
        "en": ["Arrival: clear entry", "During: find books", "Afterward: review feedback"],
        "ja": ["入場：案内を明確に", "活動中：本を探す", "終了後：感想を確認"],
    },
    "six-cards": {
        "zh-TW": ["圖書館十席", "四本短篇", "週五前通知", "週六下午", "兩人引導", "收回饋卡"],
        "en": ["Library, ten seats", "Four short books", "Invite by Friday", "Saturday afternoon", "Two facilitators", "Collect feedback"],
        "ja": ["図書館の十席", "短い本を四冊", "金曜までに案内", "土曜の午後", "進行役を二人", "感想を集める"],
    },
    "eight-cards": {
        "zh-TW": ["圖書館十席", "四本短篇", "週五前通知", "週六下午", "兩人引導", "預算待查", "通道留空", "收回饋卡"],
        "en": ["Library, ten seats", "Four short books", "Invite by Friday", "Saturday afternoon", "Two facilitators", "Check budget", "Clear passage", "Collect feedback"],
        "ja": ["図書館の十席", "短い本を四冊", "金曜までに案内", "土曜の午後", "進行役を二人", "予算を確認", "通路を空ける", "感想を集める"],
    },
    "cycle-six": {
        "zh-TW": ["觀察", "提案", "準備", "試辦", "回饋", "調整"],
        "en": ["Observe", "Propose", "Prepare", "Pilot", "Review", "Adjust"],
        "ja": ["観察", "提案", "準備", "試行", "感想", "調整"],
    },
    "mindmap-eight": {
        "zh-TW": ["社區展覽", "觀眾", "場地", "作品", "預算", "協力", "宣傳", "動線", "時間"],
        "en": ["Exhibit", "Audience", "Venue", "Works", "Budget", "Helpers", "Publicity", "Access", "Timing"],
        "ja": ["地域展示", "来場者", "会場", "作品", "予算", "協力", "周知", "動線", "時間"],
    },
    "pyramid-five": {
        "zh-TW": ["交流", "企劃", "作品", "場地", "材料"],
        "en": ["Exchange", "Planning", "Works", "Venue", "Materials"],
        "ja": ["交流", "企画", "作品", "会場", "材料"],
    },
    "seven-ideation-cards": {
        "zh-TW": ["展板", "音訊", "導覽", "書桌", "路線", "問答", "共讀"],
        "en": ["Poster", "Audio", "Tour", "Book desk", "Route", "Q&A", "Reading"],
        "ja": ["展示", "音声", "案内", "本棚", "動線", "質問", "読書"],
    },
    "fishbone-four": {
        "zh-TW": ["時段", "通知", "流程", "地點", "報名偏少"],
        "en": ["Timing", "Notices", "Process", "Location", "Low sign-ups"],
        "ja": ["時間", "周知", "手続き", "場所", "申込が少ない"],
    },
    "two-right-narrow": {
        "zh-TW": ["場地", "入口靠近書架，座位在窗邊。"],
        "en": ["Venue", "Entrance near shelves; seats by window."],
        "ja": ["会場", "入口は棚の近く、席は窓辺。"],
    },
    "matrix-3x2": {
        "zh-TW": ["館：有投影", "中心：有音響", "館：步行5分", "中心：車程15分", "館：免費", "中心：低費用"],
        "en": ["Library: projector", "Center: audio", "Library: 5 min walk", "Center: 15 min ride", "Library: free", "Center: low fee"],
        "ja": ["図書館：投影", "施設：音響", "図書館：徒歩5分", "施設：車で15分", "図書館：無料", "施設：低料金"],
    },
    "weighted-matrix": {
        "zh-TW": ["館：有投影", "中心：有音響", "亭：無設備", "館：免費", "中心：低費用", "亭：免費"],
        "en": ["Library: projector", "Center: audio", "Pavilion: none", "Library: free", "Center: low fee", "Pavilion: free"],
        "ja": ["図書館：投影", "施設：音響", "東屋：設備なし", "図書館：無料", "施設：低料金", "東屋：無料"],
    },
    "flow-five-vertical": {
        "zh-TW": ["查書", "找書", "登記", "借出", "歸還"],
        "en": ["Search", "Find", "Register", "Borrow", "Return"],
        "ja": ["検索", "探す", "登録", "借りる", "返却"],
    },
    "five-why-chain": {
        "zh-TW": ["報名少", "通知晚？", "排程晚？", "資料晚？", "責任未定？"],
        "en": ["Few sign-ups", "Late notice?", "Late plan?", "Late data?", "No owner?"],
        "ja": ["申込が少ない", "案内が遅い？", "計画が遅い？", "資料が遅い？", "担当未定？"],
    },
    "recall-strip": {
        "zh-TW": ["日照與葉色？", "窗邊葉色較深；查澆水量。", "原因仍未確定。", "遮住答案重述觀察。"],
        "en": ["Light and leaves?", "Window leaves darker; check water.", "Cause remains unclear.", "Recall with notes covered."],
        "ja": ["日照と葉色？", "窓辺は濃い。水量も調べる。", "原因はまだ不明。", "隠して観察を再現。"],
    },
    "dual-input-synthesis": {
        "zh-TW": ["人員", "書目", "小型試辦"],
        "en": ["People", "Books", "Small trial"],
        "ja": ["人", "本", "小さく試す"],
    },
    "ruled-and-sketch": {
        "zh-TW": ["入口與濾網位置", "雨水收集器草圖"],
        "en": ["Inlet and filter position", "Rain collector sketch"],
        "ja": ["入口とフィルター", "雨水収集器の図"],
    },
    "storyboard-three": {
        "zh-TW": ["入館", "找書", "討論"],
        "en": ["Enter", "Find book", "Discuss"],
        "ja": ["入館", "本を探す", "話し合う"],
    },
    "storyboard-four": {
        "zh-TW": ["入館", "找書", "閱讀", "討論"],
        "en": ["Enter", "Find book", "Read", "Discuss"],
        "ja": ["入館", "本を探す", "読む", "話し合う"],
    },
    "two-sketch-notes": {
        "zh-TW": ["入口草圖", "內部草圖"],
        "en": ["Entrance sketch", "Interior sketch"],
        "ja": ["入口の図", "内部の図"],
    },
    "mixed-storyboard": {
        "zh-TW": ["入館全景", "找書", "閱讀", "討論"],
        "en": ["Entering scene", "Find book", "Read", "Discuss"],
        "ja": ["入館の全景", "本を探す", "読む", "話し合う"],
    },
    "crazy-eight": {
        "zh-TW": ["展板", "音訊", "導覽", "書桌", "路線", "問答", "共讀", "線上"],
        "en": ["Poster", "Audio", "Tour", "Book desk", "Route", "Q&A", "Reading", "Online"],
        "ja": ["展示", "音声", "案内", "本棚", "動線", "質問", "読書", "オンライン"],
    },
    "problem-solution-three": {
        "zh-TW": ["報名偏少", "提早通知", "調整時段", "找夥伴"],
        "en": ["Low sign-ups", "Earlier notice", "New time", "Partners"],
        "ja": ["申込が少ない", "早めの案内", "時間変更", "協力者"],
    },
    "root-cause-tree": {
        "zh-TW": ["通知晚", "資訊少", "時段衝突", "交通遠", "周知", "參與門檻", "報名偏少"],
        "en": ["Late notice", "Few details", "Time clash", "Long trip", "Publicity", "Access", "Low sign-ups"],
        "ja": ["案内が遅い", "情報が少ない", "時間が合わない", "遠い", "周知", "参加条件", "申込が少ない"],
    },
    "matrix-3x3": {
        "zh-TW": ["館：有投影", "中心：有音響", "亭：無設備", "館：步行5分", "中心：車程15分", "亭：步行30分", "館：免費", "中心：低費用", "亭：免費"],
        "en": ["Library: projector", "Center: audio", "Pavilion: none", "Library: 5 min walk", "Center: 15 min ride", "Pavilion: 30 min walk", "Library: free", "Center: low fee", "Pavilion: free"],
        "ja": ["図書館：投影", "施設：音響", "東屋：設備なし", "図書館：徒歩5分", "施設：車で15分", "東屋：徒歩30分", "図書館：無料", "施設：低料金", "東屋：無料"],
    },
}

RESTORED_TEXT = {
    "problem-solution-three": {
        "zh-TW": {"title": "一題三解分岔", "purpose": "把一個觀察到的問題連向三種不同的處理方案，讓每條箭頭都表示可採取的下一步。", "when": ["活動報名偏少時，並列三種可試的改善方案。", "服務卡關時，先整理三條互不混淆的處理路徑。"], "steps": ["在左側寫具體、可觀察的問題。", "在右側三框各寫一項可執行的方案，不把猜測寫成已證實的成效。", "比較成本與待驗證條件，再決定先試哪一項。"], "unsuitable": "三條箭頭只是選項，不表示三個方案都有效或彼此獨立。", "example": "虛構讀書會的報名偏少；右側列提早通知、調整時段與找合作夥伴三種待試方案。"},
        "en": {"title": "One problem, three responses", "purpose": "Branch one observed problem toward three distinct possible actions, with arrows pointing from the question to the responses.", "when": ["List three possible responses to low event sign-ups.", "Keep service troubleshooting options separate before testing them."], "steps": ["Name an observable problem in the left box.", "Put one executable response in each right box without treating hoped-for effects as facts.", "Compare costs and open questions before choosing a first trial."], "unsuitable": "The arrows show options, not evidence that all three responses work or are independent.", "example": "A fictional reading group has low sign-ups; earlier notice, a different time, and partners are three untested responses."},
        "ja": {"title": "一つの問題から三つの対応", "purpose": "観察した問題から三つの対応案へ矢印を分け、問いから対策へ進む方向を示します。", "when": ["催しの申込が少ないときに三つの対応を比べる場合。", "サービスの問題に対する選択肢を試す前に分ける場合。"], "steps": ["左の枠に観察できる問題を書きます。", "右の三枠に実行できる案を一つずつ書き、期待だけで効果を断定しません。", "費用と未確認の条件を比べ、最初の試行を決めます。"], "unsuitable": "矢印は選択肢を示すだけで、三案すべての効果や独立性を証明しません。", "example": "架空の読書会で申込が少ない場合、早めの案内、時間変更、協力者を未検証の案として並べます。"},
    },
    "root-cause-tree": {
        "zh-TW": {"title": "原因匯流樹", "purpose": "由四個原因候選經兩個類別匯向一個觀察結果，檢視哪些連結仍需查證。", "when": ["把報名偏少的原因假設按周知與參與門檻整理。", "追查流程錯誤是否來自兩組不同條件。"], "steps": ["最下方寫可觀察結果。", "上方四格分別寫原因候選，中間兩格為可解釋的群組。", "沿箭頭回查每條關係的證據，刪掉無法支持的連結。"], "unsuitable": "線條不構成因果證明；若原因互相影響，改用網絡圖或另外記錄資料。", "example": "虛構活動的晚通知、資訊少、時段衝突及交通遠先歸為周知與參與門檻，最後指向報名偏少；全部仍是待驗證假設。"},
        "en": {"title": "Converging root-cause tree", "purpose": "Bring four candidate causes through two groups toward one observed outcome, keeping each causal link open to checking.", "when": ["Group possible reasons for low sign-ups into publicity and access conditions.", "Investigate whether two kinds of conditions contribute to a process error."], "steps": ["Write an observable outcome at the bottom.", "Place four candidate causes above and name two explanatory groups in the middle.", "Trace every arrow back to evidence and remove unsupported links."], "unsuitable": "A drawn arrow is not causal proof; use a network or separate evidence notes when causes interact.", "example": "Late notice, few details, a time clash, and a long trip are grouped as publicity and access hypotheses before pointing to low sign-ups."},
        "ja": {"title": "原因が集まる樹形図", "purpose": "四つの原因候補を二群にまとめ、一つの観察結果に向けて因果の仮説を点検します。", "when": ["申込が少ない理由を周知と参加条件に分ける場合。", "作業の誤りに二種類の条件が関わるか調べる場合。"], "steps": ["最下段に観察できる結果を書きます。", "上の四枠に候補、中間の二枠に説明できる群を書きます。", "各矢印の根拠を調べ、支えられない関係は外します。"], "unsuitable": "描いた矢印だけでは因果を証明できません。要因同士が影響し合う場合は別の図や根拠の記録が必要です。", "example": "案内の遅れ、情報不足、時間の衝突、遠い移動を周知と参加条件の仮説としてまとめ、申込減少につなぎます。"},
    },
    "matrix-3x3": {
        "zh-TW": {"title": "三乘三比較矩陣", "purpose": "用九個等大連續儲存格，交叉記錄三個方案與三項條件；沒有九宮格的中心向外發想語意。", "when": ["比較三種場地的設備、交通與費用。", "核對三份來源對三個相同問題的回答。"], "steps": ["先在紙邊自訂三欄方案與三行條件。", "每格只填對應交叉項的短證據，缺資料就保留空白。", "逐行逐欄比較，另外記錄證據來源與單位。"], "unsuitable": "九格不會自動表示中心主題；精確評分需另列單位與權重。", "example": "虛構的圖書館、社區中心、戶外亭分別在設備、交通與費用三行留下待核對的短記。"},
        "en": {"title": "Three-by-three comparison matrix", "purpose": "Use nine equal adjoining cells for three options crossed with three criteria, without a mandala's center-outward idea behavior.", "when": ["Compare equipment, travel, and cost for three venues.", "Check how three sources answer the same three questions."], "steps": ["Define three column options and three row criteria in your own notes.", "Put brief evidence for each intersection in its cell; leave missing data blank.", "Compare across rows and columns while recording sources and units separately."], "unsuitable": "Nine cells do not imply a central topic; precise scores require units and weighting outside this sheet.", "example": "A fictional library, community center, and pavilion are checked across equipment, travel, and cost, with each cell holding a short item to verify."},
        "ja": {"title": "三行三列の比較表", "purpose": "九つの同じ大きさのマスで三案と三条件を交差させ、中心から広げる九宮の使い方とは分けます。", "when": ["三会場の設備、交通、費用を比べる場合。", "三つの資料が同じ三問にどう答えるか調べる場合。"], "steps": ["三列の案と三行の条件を自分のメモで定めます。", "交差するマスに短い根拠を書き、不明な箇所は空けておきます。", "行と列を見比べ、出典や単位は別に記します。"], "unsuitable": "九マスだけでは中心テーマを示しません。正確な採点には単位と重みが必要です。", "example": "架空の図書館、地域施設、東屋について、設備、交通、費用の各マスに確かめる短い記録を置きます。"},
    },
}

ALIAS_FOCUS = {
    "mirrored-compare-cards": ("以四張卡成對比較兩個場地。", "Pair four cards to compare two venues.", "四枚のカードで二会場を対にして比べます。"),
    "causal-chain": ("把四個待驗證的原因與結果假設串成單一路徑。", "Link four untested cause-and-effect hypotheses in one path.", "四つの未確認の因果仮説を一つの経路に並べます。"),
    "frayer": ("中央寫概念，四區分開定義、特徵、例子與非例。", "Put a concept in the center, then separate meaning, traits, example, and nonexample.", "中央の概念から定義、特徴、例、非例を分けます。"),
    "cue-answer": ("窄欄放提問線索，寬欄放可查證的回答。", "Put a retrieval cue in the narrow column and a checkable answer in the wide one.", "細い欄に手がかり、広い欄に確認できる答えを書きます。"),
    "concept-examples-six": ("中央寫概念，六個外圈各放一個具體例子。", "Put one concept at the center and a concrete example on each of six branches.", "中心に概念を置き、六つの枝に具体例を書きます。"),
    "quote-side-notes": ("寬欄保留短引文，窄欄記來源或待查問題。", "Keep a short quotation in the wide column and source questions at its side.", "広い欄に短い引用、細い欄に出典の確認点を置きます。"),
    "quote-comment-parallel": ("左右並列虛構引文與自己的查證評論。", "Place a fictional quotation beside a separate checkable comment.", "架空の引用と確認が必要なコメントを左右に分けます。"),
    "observation-interpretation": ("一欄記直接觀察，另一欄記暫時解釋，避免混為事實。", "Separate direct observation from a tentative interpretation.", "直接の観察と仮の解釈を別の欄に分けます。"),
    "source-large-plus-cards": ("主卡標示資料，三小卡記主張、依據與待查之處。", "Name a source in the large card and use three smaller cards for claim, evidence, and question.", "大きいカードに資料、小さい三枚に主張、根拠、確認点を記します。"),
    "research-index-cards": ("三卡記不同來源，第四卡記待核對的衝突。", "Record three distinct sources and one unresolved conflict on four cards.", "三枚に異なる資料、四枚目に未確認の食い違いを記します。"),
    "pixel-stitch-grid": ("用格子記錄像素或針織色塊，另外標出材料問題。", "Plan pixel or stitch color blocks on the grid and note a material question.", "マスに画素や編み目の色を置き、材料の確認点も記します。"),
}

ALIAS_TITLES = {
    "mirrored-compare-cards": ("成對比較卡", "Paired comparison cards", "対になる比較カード"),
    "causal-chain": ("因果假設鏈", "Causal hypothesis chain", "因果仮説の連鎖"),
    "frayer": ("Frayer 概念四分圖", "Frayer concept map", "フレイヤーの概念図"),
    "cue-answer": ("線索與回答", "Cue and answer", "手がかりと答え"),
    "concept-examples-six": ("概念與六個例子", "Concept and six examples", "概念と六つの例"),
    "quote-side-notes": ("引文與旁註", "Quotation with side notes", "引用と欄外メモ"),
    "quote-comment-parallel": ("引文與評論對照", "Quotation and comment", "引用とコメント"),
    "observation-interpretation": ("觀察與解釋", "Observation and interpretation", "観察と解釈"),
    "source-large-plus-cards": ("資料主卡與三註", "Source card and three notes", "資料カードと三つのメモ"),
    "research-index-cards": ("研究索引四卡", "Four research index cards", "調査用の四枚の索引カード"),
    "pixel-stitch-grid": ("像素與針織方格", "Pixel and stitch grid", "画素と編み目の方眼"),
}

VARIANT_TITLES = {
    "ruled-narrow": ("窄行距橫線", "Narrow ruled notes", "細い横罫ノート"),
    "ruled-wide": ("寬行距橫線", "Wide ruled notes", "広い横罫ノート"),
    "grid-fine": ("細方格", "Fine square grid", "細かい方眼"),
    "grid-large": ("大方格", "Large square grid", "大きい方眼"),
    "dot-fine": ("細點陣", "Fine dot grid", "細かいドット方眼"),
    "cornell-mirrored": ("康乃爾式筆記頁（右提示欄）", "Mirrored Cornell notes", "右に手がかり欄のコーネル式"),
    "fishbone-four": ("四組原因魚骨圖", "Four-branch fishbone", "四組の魚骨図"),
    "storyboard-three": ("三格故事板", "Three-panel storyboard", "三コマの絵コンテ"),
    "storyboard-four": ("四格故事板", "Four-panel storyboard", "四コマの絵コンテ"),
    "isometric-grid": ("等角三角格", "Isometric triangular grid", "等角三角グリッド"),
    "engineering-grid": ("工程主線方格", "Engineering grid", "主線つき方眼"),
    "two-right-narrow": ("右窄欄筆記", "Narrow right column", "右側が細い二段組"),
    "three-stacked-cards": ("上下三卡", "Three stacked cards", "縦に三枚のカード"),
    "six-cards": ("六張獨立卡", "Six separate cards", "六枚の独立カード"),
    "eight-cards": ("八張獨立卡", "Eight separate cards", "八枚の独立カード"),
    "cross-compare": ("交叉比較四區", "Cross comparison", "交差比較の四区画"),
    "matrix-3x2": ("二欄三行比較矩陣", "Two-by-three comparison matrix", "二列三行の比較表"),
    "axis-matrix": ("座標軸比較", "Axis comparison matrix", "座標軸の比較表"),
    "weighted-matrix": ("不等寬比較矩陣", "Weighted-size matrix", "幅の異なる比較表"),
    "flower-six": ("六瓣發想花", "Six-petal idea flower", "六つの花びらの発想図"),
    "flow-five-vertical": ("五步直向流程", "Five-step vertical flow", "縦の五段階フロー"),
    "cycle-six": ("六段循環", "Six-stage cycle", "六段階の循環"),
    "causal-chain": ("因果假設鏈", "Causal hypothesis chain", "因果仮説の連鎖"),
    "five-why-chain": ("五層追問鏈", "Five-whys chain", "五回のなぜの連鎖"),
    "mindmap-eight": ("八分枝心智圖", "Eight-branch mind map", "八枝のマインドマップ"),
    "bottom-up-tree": ("由下而上樹圖", "Bottom-up tree", "下から上への樹形図"),
    "pyramid-five": ("五層金字塔", "Five-tier pyramid", "五段のピラミッド"),
    "recall-strip": ("康乃爾式筆記頁（附回想條）", "Cornell notes with recall strip", "想起欄つきコーネル式"),
    "crazy-eight": ("八格快速發想", "Crazy eight idea sketch", "八コマの速い発想"),
    "idea-bubbles-six": ("六泡發想圖", "Six-bubble idea map", "六つの吹き出しの発想図"),
    "hero-idea-seven-variations": ("主構想與七變化", "Hero idea with seven variations", "中心案と七つの変化"),
    "dual-input-synthesis": ("雙輸入綜合圖", "Two-input synthesis", "二つの入力をまとめる図"),
    "seven-ideation-cards": ("七張發想卡", "Seven ideation cards", "七枚の発想カード"),
    "two-sketch-notes": ("雙草圖筆記", "Two sketch notes", "二枚の下書きノート"),
    "mixed-storyboard": ("大小交錯四格故事板", "Mixed-scale four-panel storyboard", "大小混合の四コマ絵コンテ"),
    "pixel-stitch-grid": ("像素與針織方格", "Pixel and stitch grid", "画素と編み目の方眼"),
    "ruled-and-sketch": ("上線下圖筆記", "Ruled notes above sketch", "上に横罫、下に下書き"),
}

# Explain what a parameter changes in the actual writing method. These
# descriptions are shared only when the operation really has the same method.
# Functional aliases and restored independent layouts override them below.
OPERATION_PURPOSE = {
    "mirror_x": ("將提示或補註放在右側窄欄，主筆記留在較寬的左側。", "Put cues or side notes in the narrow right region and main notes in the wider left region.", "右の細い欄に手がかりや注記を置き、左の広い欄に本文を書きます。"),
    "mirror_y": ("從下方細項向上彙整為較高層的結論。", "Build upward from details toward a broader conclusion.", "下の細部から上位のまとめへ組み立てます。"),
    "fishbone": ("把觀察到的問題和多組可能原因分開，逐條追問支因。", "Separate an observed problem from several groups of possible causes and their subcauses.", "観察した問題と複数の原因候補、その下位要因を分けます。"),
    "storyboard": ("用連續畫格描繪同一事件的變化，並在每格留下動作提示。", "Show successive changes in one event, with a short action cue for every frame.", "一つの出来事の変化を連続したコマに描き、各コマに短い動作を添えます。"),
    "stacked_cards": ("將前、中、後三段資訊分開記錄，再檢查順序。", "Keep before, during, and after entries in three separate stacked cards.", "前・中・後の情報を三枚の縦のカードに分け、順序を確かめます。"),
    "card_grid": ("將多個候選想法放進各自的獨立卡片，再比較或排序。", "Give each candidate idea its own card before comparing or ordering them.", "候補の考えを一枚ずつ独立したカードに置き、比べたり並べたりします。"),
    "matrix": ("先定義橫向方案與縱向條件，再逐格記錄交叉資訊。", "Define options along one direction and criteria along the other, then fill their intersections.", "一方に案、もう一方に条件を決め、交差するマスを埋めます。"),
    "weighted_matrix": ("以不同寬度保留較多書寫空間，但仍以同一條件比較方案。", "Allow unequal writing space while comparing options against the same criteria.", "書く量に応じて幅を変えながら、同じ条件で案を比べます。"),
    "flower": ("從中心主題向周圍六個泡泡延伸不同想法。", "Expand one central topic into six distinct surrounding idea bubbles.", "中心の話題から周囲の六つの吹き出しへ考えを広げます。"),
    "vertical_flow": ("由上到下追蹤五個連續步驟，留意每一步的輸入與結果。", "Trace five consecutive steps from top to bottom and check each transition.", "上から下へ五つの連続した段階を追い、つながりを確かめます。"),
    "cycle": ("將六個階段排成可回到起點的循環，記錄每次調整。", "Arrange six stages as a repeatable loop and record what changes on the next pass.", "六段階を出発点に戻る循環として並べ、次回の調整を記録します。"),
    "mindmap": ("以中心主題連向八個不同面向，再檢查哪些需要次級概念。", "Connect a central topic to eight distinct branches and mark where subtopics are needed.", "中心から八つの異なる枝を広げ、下位の話題が必要な枝を見つけます。"),
    "pyramid": ("把基礎條件、行動與上層目標分成五層，檢查支撐關係。", "Arrange foundations, actions, and the goal into five tiers and inspect their support.", "土台、行動、目標を五段に分け、支える関係を確かめます。"),
    "recall_strip": ("在康乃爾筆記下方另設回想區，遮住答案後自我測試。", "Add a separate recall strip below Cornell notes for a cover-and-recall check.", "コーネル式の下に想起欄を設け、答えを隠して確かめます。"),
    "center_satellites": ("先畫中心主構想，再將七種變化分放周圍卡片。", "Keep one main proposal in the center and test seven variations around it.", "中心に主案を置き、周囲の七枚で変化案を試します。"),
    "converging_flow": ("由兩項不同輸入共同推向一個暫定綜合結果。", "Bring two different inputs toward one provisional synthesis.", "異なる二つの入力を一つの暫定的なまとめへつなげます。"),
    "mixed_storyboard": ("用一個大畫面建立場景，再以三個小畫格展示後續動作。", "Establish a scene in one large frame, then show three subsequent beats in smaller frames.", "大きい一コマで場面を示し、後の三つの動きを小さなコマに描きます。"),
    "ruled_sketch_bottom": ("上方先記重點，下方以草圖驗證位置與比例。", "Write key notes above and test placement and proportion in a sketch below.", "上に要点を書き、下の草図で位置と比率を確かめます。"),
}

FUNCTIONAL_PURPOSE = {
    "cornell-mirrored": ("把康乃爾提示欄移到右側，左側保留主筆記，下方總結用於回想。", "Move the Cornell cue column to the right, keeping main notes on the left and a summary below for recall.", "コーネル式の手がかり欄を右に移し、左に本文、下に想起用のまとめを残します。"),
    "two-right-narrow": ("將短來源與待查問題放在右側窄欄，左側留給連續筆記或草圖。", "Put short references and open questions in the narrow right column, leaving the left for continuous notes or sketches.", "右の細い欄に短い出典や確認点を置き、左に本文や下書きを残します。"),
    "isometric-grid": ("利用三方向等距格線構思等角物件，尺寸仍須另行量測。", "Use the three-direction lattice to sketch equal-angle objects; verify actual dimensions separately.", "三方向の等間隔線で等角の物を下書きし、実寸は別に測ります。"),
    "cross-compare": ("以兩個選定標準把四個方案分入交叉區域，比較取捨。", "Place four options on two chosen criteria and compare their tradeoffs across the cross.", "二つの基準で四案を交差する領域に置き、取捨を比べます。"),
    "axis-matrix": ("將方案放在有刻度的兩軸上，核對方向與相對位置。", "Plot options on two ticked axes and check their direction and relative position.", "目盛りのある二軸に案を置き、方向と相対位置を確かめます。"),
    "crazy-eight": ("在八格各畫一個快速構想，先保留差異，之後才篩選。", "Sketch one quick idea in each of eight cells, preserving differences before selection.", "八コマに素早く一案ずつ描き、違いを残してから選びます。"),
    "five-why-chain": ("由觀察到的問題連續追問為什麼，逐層記錄待查證的原因假設。", "Ask why repeatedly from an observed problem, recording each answer as a hypothesis to check.", "観察した問題から『なぜ』を重ね、各答えを確かめる仮説として残します。"),
    "idea-bubbles-six": ("把同一主題周圍六個不同構想分開記錄，暫不排序。", "Keep six distinct possibilities around one topic without ranking them yet.", "一つの話題の周囲に六つの異なる案を置き、まだ順位を決めません。"),
}


OPERATION_ACTION = {
    "mirror_x": ("先按左右鏡像後的位置指定提示區、主內容區與摘要區的角色。", "Assign cue, main-note and summary roles using the mirrored left/right positions.", "左右反転後の位置に合わせ、手がかり・本文・要約の役割を決めます。"),
    "mirror_y": ("從下方的上位主題開始，向上拆成群組與細項。", "Start with the parent topic at the bottom and split upward into groups and details.", "下の上位主題から上へ、群と細目に分けます。"),
    "card_grid": ("先決定各卡是不同方案還是同一主題的不同面向，每張只放一個可比較單位。", "Decide whether cards hold options or facets of one topic; use one comparable unit per card.", "各カードを案か観点に割り当て、一枚に比較できる単位を一つ置きます。"),
    "stacked_cards": ("由上到下為各卡指定一項主題，讓文字與證據留在同一卡內。", "Assign one topic to each card from top to bottom, keeping its notes and evidence together.", "上から各カードに一つの話題を割り当て、記録と根拠をまとめます。"),
    "storyboard": ("先把事件分成與本頁畫格數相符的關鍵場景，每格畫出可見的變化。", "Divide the event into the number of frames on this page and draw a visible change in each.", "このページのコマ数に合わせて場面を分け、各コマに見える変化を描きます。"),
    "fishbone": ("魚頭寫問題，每條主枝放一類原因，沿支枝補上可查證的條件。", "Put the problem at the head, a cause category on each main bone and checkable conditions on sub-branches.", "頭に問題、主枝に原因の分類、下位の枝に確かめる条件を書きます。"),
    "matrix": ("先為列與欄設定不同的比較維度，再逐格填入交叉處的資料。", "Define different dimensions for rows and columns, then fill their intersections.", "行と列に異なる比較軸を決め、交点の情報を記入します。"),
    "weighted_matrix": ("先將較寬的欄或較高的列分配給需要更多說明的項目；面積不代表分數。", "Assign larger cells to entries needing more explanation; cell area is not a score.", "説明量に合わせて広いマスを割り当て、面積を点数と混同しません。"),
    "vertical_flow": ("由上到下填入五個相接的步驟或追問，每支箭頭只連接相鄰兩格。", "Fill five connected steps or questions from top to bottom; each arrow links neighboring boxes.", "上から五つの手順または問いを記し、矢印で隣の枠につなぎます。"),
    "cycle": ("沿同一旋轉方向填入各階段，最後一格要能回到起點。", "Fill stages in one rotational direction and check how the last returns to the first.", "一定の回転方向で段階を記し、最後から最初へ戻る条件を確認します。"),
    "flower": ("中央寫主題，外圈每個圓放一個不同面向，避免重複詞。", "Put the topic in the center and a distinct facet in each outer circle.", "中心に主題、外側の円に重複しない観点を置きます。"),
    "mindmap": ("中央寫主題，每條分枝放一個主要概念，再向外補充次級概念。", "Place the topic in the center, one main concept on each spoke and supporting ideas farther out.", "中心に主題、各枝に主要概念、その先に補足の概念を置きます。"),
    "pyramid": ("先決定由基礎到上層的層級意義，每層只寫同一尺度的項目。", "Define the hierarchy from foundation to top and keep entries at each level comparable.", "土台から上へ階層の意味を決め、各段に同じ尺度の項目を書きます。"),
    "center_satellites": ("中央放核心方案，外側各卡放一個改動方向，再比較取捨。", "Put the core proposal in the center and one modification on each outer card.", "中心に基本案、外側の各カードに一つの変更案を置きます。"),
    "converging_flow": ("左側各框放一個輸入來源，右側寫整合結果，沿箭頭說明來源貢獻。", "Place an input in each left box and the synthesis on the right, tracing each contribution.", "左の枠に入力、右に統合結果を書き、矢印に沿って各寄与を確認します。"),
    "mixed_storyboard": ("大框畫背景全景，下方三小框畫接續的動作或細節。", "Draw the establishing view in the large frame and three actions or details below.", "大枠に全景、下の三枠に続く動作や細部を描きます。"),
    "ruled_sketch_bottom": ("上方橫線記文字線索，下方畫對應草圖，標出圖文間的關係。", "Record verbal cues on the upper lines and a related sketch below, marking their links.", "上の罫線に言葉の手がかり、下に対応する図を描き、関係を示します。"),
}


def make_variant_content(content: dict, profile: dict, builders: dict) -> dict:
    result = {}
    for layout_id, (classification, operation, value) in VARIANT_METHODS.items():
        target = ORIGINAL_MERGES[layout_id]["target"]
        original = content.get(target, result.get(target))
        if original is None:
            raise ValueError(f"Variant target must precede its alias: {target}")
        item = {"source_type": original["source_type"],
                "source_note": f"{classification} of {target}. {ORIGINAL_MERGES[layout_id]['reason']}",
                "variant_of": target, "variant_classification": classification,
                "translations": {}}
        scene = Scene.from_profile(profile)
        builders[layout_id](scene, profile)
        for lang, t in original["translations"].items():
            c = COMMON[lang]
            change = change_text(operation, value, lang)
            if layout_id in SPECIAL_LABELS:
                labels = SPECIAL_LABELS[layout_id][lang]
            elif classification == "equivalent":
                labels = deepcopy(t["labels"])
            else:
                labels = deepcopy(t["labels"][:len(scene.slots)])
                extra = {"zh-TW": "補充", "en": "Next", "ja": "追加"}[lang]
                while len(labels) < len(scene.slots):
                    labels.append(f"{extra} {len(labels) + 1}")
            if len(labels) != len(scene.slots):
                raise ValueError(f"Variant label count: {layout_id}/{lang}")
            item["translations"][lang] = {
                "title": VARIANT_TITLES.get(layout_id, (f"{c['title']} · {layout_id}",) * 3)[("zh-TW", "en", "ja").index(lang)],
                "purpose": f"{t['purpose']} {c['extra']} {change}",
                "when": list(t["when"]), "steps": list(t["steps"]),
                "unsuitable": t["unsuitable"] if c["unsuitable"] in t["unsuitable"] else f"{t['unsuitable']} {c['unsuitable']}",
                "example": f"{t['example']} {c['example']}",
                "labels": labels,
            }
            if operation in ("ruled", "grid", "dot", "engineering_grid"):
                item["translations"][lang]["steps"] = list(t["steps"])
            if operation not in ("ruled", "grid", "dot", "engineering_grid", "recall_strip"):
                item["translations"][lang]["purpose"] = f"{c['use']} {c['extra']} {change}"
                item["translations"][lang]["when"] = list(t["when"])
                item["translations"][lang]["example_entries"] = deepcopy(labels)
                item["translations"][lang]["example"] = region_example(labels, lang)
                item["content_revision"] = 3
            if operation in OPERATION_PURPOSE:
                method = OPERATION_PURPOSE[operation][("zh-TW", "en", "ja").index(lang)]
                item["translations"][lang]["purpose"] = f"{method} {c['extra']} {change}"
                item["translations"][lang]["steps"][0] = method
            if layout_id in ALIAS_FOCUS:
                item["translations"][lang]["title"] = ALIAS_TITLES[layout_id][("zh-TW", "en", "ja").index(lang)]
                item["translations"][lang]["purpose"] = ALIAS_FOCUS[layout_id][("zh-TW", "en", "ja").index(lang)]
                item["translations"][lang]["unsuitable"] = c["unsuitable"]
                item["translations"][lang]["steps"][0] = item["translations"][lang]["purpose"]
            if layout_id in FUNCTIONAL_PURPOSE:
                item["translations"][lang]["purpose"] = FUNCTIONAL_PURPOSE[layout_id][("zh-TW", "en", "ja").index(lang)]
                item["translations"][lang]["steps"][0] = item["translations"][lang]["purpose"]
            if operation in OPERATION_ACTION:
                index = ("zh-TW", "en", "ja").index(lang)
                sample = ("參考本頁示例，各區依序記錄：", "Use the worked example to place entries in region order: ", "記入例を参考に、領域の順で記します：")[index]
                check = ("回看各區，標記仍待查證的內容，再決定下一步。", "Review the regions, mark open questions and choose a next step.", "各領域を読み返し、未確認の点と次の行動を記します。")[index]
                item["translations"][lang]["steps"] = [OPERATION_ACTION[operation][index], sample + inline_entries(labels, lang), check]
                item["content_revision"] = 3
            if layout_id in RESTORED_TEXT:
                item["translations"][lang].update(RESTORED_TEXT[layout_id][lang])
                if "example" in RESTORED_TEXT[layout_id][lang]:
                    item["translations"][lang].pop("example_entries", None)
        result[layout_id] = item
    scenarios = json.loads((Path(__file__).resolve().parents[2] / "content/usage-scenarios.json").read_text(encoding="utf-8"))
    for layout_id, translations in scenarios.items():
        if layout_id not in result or set(translations) != {"zh-TW", "en", "ja"}:
            raise ValueError(f"Invalid usage scenario ID or languages: {layout_id}")
        for lang, examples in translations.items():
            if len(examples) != 2 or any(not isinstance(value, str) or not value.strip() for value in examples):
                raise ValueError(f"Invalid usage scenarios: {layout_id}/{lang}")
            result[layout_id]["translations"][lang]["when"] = examples
        result[layout_id]["content_revision"] = max(2, result[layout_id].get("content_revision", 1))
    guidance = json.loads((Path(__file__).resolve().parents[2] / "content/method-guidance.json").read_text(encoding="utf-8"))
    for layout_id, translations in guidance.items():
        if layout_id not in result or set(translations) != {"zh-TW", "en", "ja"}:
            raise ValueError(f"Invalid method guidance: {layout_id}")
        for lang, fields in translations.items():
            if not fields or set(fields) - {"steps", "unsuitable"}:
                raise ValueError(f"Invalid method guidance fields: {layout_id}/{lang}")
            result[layout_id]["translations"][lang].update(fields)
    limitations = json.loads((Path(__file__).resolve().parents[2] / "content/format-limitations.json").read_text(encoding="utf-8"))
    for layout_id, translations in limitations.items():
        if layout_id not in result or set(translations) != {"zh-TW", "en", "ja"}:
            raise ValueError(f"Invalid format limitation: {layout_id}")
        for lang, text in translations.items():
            if not isinstance(text, str) or not text.strip():
                raise ValueError(f"Empty format limitation: {layout_id}/{lang}")
            result[layout_id]["translations"][lang]["unsuitable"] = text
        result[layout_id]["content_revision"] = 3
    return result

from datetime import date
from collections import defaultdict

# ─────────────────────────────────────────
# データ定義
# ─────────────────────────────────────────

CDS = [
    {
        "id": 0,
        "label": "視聴盤 Vol.1",
        "color": "#7F77DD",  # purple-400
        "tracks": [
            ("CANNABIS", "COUNT DOWN",                  date(1999, 10, 28)),
            ("スケボーキング", "ビンゴ",                 date(2000,  1, 26)),
            ("ノーナ・リーヴス", "STOP ME",              date(1999, 11, 10)),
            ("キリンジ", "アルカディア",                  date(2000,  1, 19)),
            ("クラムボン", "はなれ ばなれ",              date(1999,  3, 25)),
            ("SPANOVA", "UNTITLED",                      date(1999,  5, 26)),
            ("ハーベスト", "FEELIN' GROOVY",             date(1999, 12, 10)),
            ("アナム☆マキ", "Good Night (デモ)",         date(2000,  9, 27)),
            ("SUPERHYPE", "TRUE",                        date(1999,  9, 30)),
            ("FOOT STAMP", "大人",                       date(2000,  2, 24)),
            ("HERMANN H", "靴底",                        date(1999, 10,  7)),
            ("WiTH MY FOOT", "MAKE MY WAY",             date(1999, 11, 11)),
            ("桔梗", "まぶたを開いたまま",               date(2000,  2, 24)),
            ("ester rina", "満点グライダー",              date(2000,  1, 27)),
            ("TAMAMI", "BYE",                            date(2000,  2, 24)),
        ],
    },
    {
        "id": 1,
        "label": "視聴盤 Vol.2",
        "color": "#1D9E75",  # teal-400
        "tracks": [
            ("花＊花", "あ〜よかった",                    date(2000,  7, 26)),
            ("TOMATO CUBE", "うたかた",                  date(2000,  7, 26)),
            ("スケボーキング", "CHILD REPLAY",           date(2000,  8, 23)),
            ("CANNABIS", "妄想R",                        date(2000,  8, 23)),
            ("BOaT", "狂言メッセージ",                   date(2000,  6, 21)),
            ("クラムボン", "君は僕のもの",               date(2000,  8,  9)),
            ("アナム&マキ", "戦え！野良犬",              date(2000,  7, 12)),
            ("キリンジ", "君の胸に抱かれたい",           date(2000,  7, 12)),
            ("SUPERHYPE", "NUMBER FUTURE",               date(2000,  8,  9)),
            ("RYO the Skywalker", "SUNNY DAY WALK",      date(2000,  8,  9)),
            ("Hermann H.", "Loser's Parade",             date(2000,  3, 24)),
            ("esterrina", "すてきな空",                   date(2000,  5, 25)),
            ("THE PAN", "かわらないもの",                date(2000,  5, 25)),
            ("ギャラクティカ★マグナム", "夕凪",          date(2000,  6, 22)),
            ("VooDoo Hawaiians", "番犬",                 date(2000,  7, 27)),
        ],
    },
    {
        "id": 2,
        "label": "視聴盤 Vol.3",
        "color": "#D85A30",  # coral-400
        "tracks": [
            ("花＊花", "さよなら大好きな人",             date(2000, 10, 25)),
            ("クラムボン", "ドギー&マギー",              date(2000, 10, 25)),
            ("キリンジ", "エイリアンズ",                  date(2000, 10, 12)),
            ("ノーナ・リーブス", "DJ!DJ!",               date(2000,  9, 13)),
            ("TOMATO CUBE", "桜",                        date(2000, 11,  8)),
            ("アナム＆マキ", "Good Night",               date(2000,  9, 27)),
            ("花＊花", "あ〜良かった (setagaya mix)",     date(2000,  7, 26)),
            ("クラムボン", "君は僕のもの",               date(2000,  8,  9)),
            ("キリンジ", "イカロスの末裔",               date(2000, 10, 12)),
            ("ノーナ・リーヴス", "二十歳の夏",           date(2000, 10, 12)),
            ("TOMATO CUBE", "うたかた",                  date(2000,  7, 26)),
            ("アナム＆マキ", "戦え！野良犬",             date(2000,  7, 12)),
        ],
    },
    {
        "id": 3,
        "label": "2001 Vol.1",
        "color": "#378ADD",  # blue-400
        "tracks": [
            ("コブクロ", "YELL〜エール〜",               date(2001,  3, 22)),
            ("CANNABIS", "経験",                         date(2001,  4, 25)),
            ("キリンジ", "グッディ・グッバイ",           date(2001,  4, 25)),
            ("アナム&マキ", "春",                        date(2000, 11, 22)),
            ("TOMATO CUBE", "桜",                        date(2000, 11,  8)),
            ("TOMATO CUBE", "私がいるよ",                date(2001,  4, 25)),
            ("BOAT", "CIRCLE SOUND",                     date(2001,  4, 11)),
            ("NONA REEVES", "LOVE TOGETHER (バラッパMIX)", date(2001, 5,  9)),
            ("THE PAN", "ひばり",                        date(2000, 10, 26)),
            ("Hermann H.", "夜には星と音楽を",           date(2001,  1, 26)),
            ("What's Love?", "泣けるほど",               date(2001,  1, 26)),
            ("FOOT STAMP", "人",                         date(2000, 10, 26)),
            ("PHEW PHEW L!VE", "on and on",              date(2000, 10, 26)),
        ],
    },
    {
        "id": 4,
        "label": "13曲1000円",
        "color": "#BA7517",  # amber-400
        "tracks": [
            ("コブクロ", "Bell",                         date(2001,  3, 22)),
            ("クラムボン", "サラウンド",                 date(2001,  5, 23)),
            ("キリンジ", "エイリアンズ",                  date(2000, 10, 12)),
            ("ノーナ・リーブス", "LOVE TOGETHER",        date(2000,  3, 23)),
            ("森広隆", "ただ時が経っただけで",           date(2001,  6, 15)),
            ("アナム＆マキ", "戦え！野良犬",             date(2000,  7, 12)),
            ("TOMATO CUBE", "choose my life",            date(2001,  5, 23)),
            ("THE PAN", "情熱",                          date(2001,  6,  6)),
            ("FOOT STAMP", "人",                         date(2000,  9, 28)),
            ("CANNABIS", "誓いの空",                     date(2001,  7, 11)),
            ("BOAT", "ALL",                              date(2001,  4, 11)),
            ("Hermann H.", "fruity machine gun",         date(2000,  3, 24)),
            ("What's Love?", "かえり路",                 date(2001,  6,  6)),
        ],
    },
]

# ─────────────────────────────────────────
# レイアウト定数
# ─────────────────────────────────────────

DATE_MIN = date(1999,  1,  1)
DATE_MAX = date(2002,  1,  1)

MARGIN_LEFT   = 160   # ラベル列の幅
MARGIN_RIGHT  = 24
MARGIN_TOP    = 60
MARGIN_BOTTOM = 50

PLOT_W = 780          # プロット領域の横幅
LANE_H = 90           # 1レーン（CD）の高さ
R      = 5            # 点の半径

N_LANES = len(CDS)
TOTAL_H = MARGIN_TOP + N_LANES * LANE_H + MARGIN_BOTTOM
TOTAL_W = MARGIN_LEFT + PLOT_W + MARGIN_RIGHT

FONT = "Noto Sans JP, Hiragino Kaku Gothic Pro, Meiryo, sans-serif"


def date_to_x(d: date) -> float:
    total = (DATE_MAX - DATE_MIN).days
    elapsed = (d - DATE_MIN).days
    return MARGIN_LEFT + PLOT_W * elapsed / total


def lane_cy(lane_idx: int) -> float:
    return MARGIN_TOP + lane_idx * LANE_H + LANE_H / 2


def year_ticks():
    ticks = []
    for yr in range(1999, 2003):
        d = date(yr, 1, 1)
        x = date_to_x(d)
        ticks.append((x, str(yr)))
    return ticks


# ─────────────────────────────────────────
# SVG生成
# ─────────────────────────────────────────

def esc(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;"))


lines = []
w = TOTAL_W
h = TOTAL_H

lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
             f'viewBox="0 0 {w} {h}" style="background:#fafaf7; font-family:{FONT};">')

# ── 背景ストライプ ──
for i, cd in enumerate(CDS):
    cy = lane_cy(i)
    y0 = cy - LANE_H / 2
    fill = "#f4f3ee" if i % 2 == 0 else "#fafaf7"
    lines.append(f'  <rect x="0" y="{y0:.1f}" width="{w}" height="{LANE_H}" fill="{fill}"/>')

# ── 年グリッド ──
for x, label in year_ticks():
    lines.append(f'  <line x1="{x:.1f}" y1="{MARGIN_TOP - 20}" x2="{x:.1f}" '
                 f'y2="{TOTAL_H - MARGIN_BOTTOM + 10}" '
                 f'stroke="#c8c6be" stroke-width="1" stroke-dasharray="4 4"/>')
    lines.append(f'  <text x="{x:.1f}" y="{TOTAL_H - MARGIN_BOTTOM + 26}" '
                 f'text-anchor="middle" font-size="13" fill="#888780">{esc(label)}</text>')
    lines.append(f'  <text x="{x:.1f}" y="{MARGIN_TOP - 6}" '
                 f'text-anchor="middle" font-size="13" fill="#888780">{esc(label)}</text>')

# ── 月グリッド（薄め）──
for yr in range(1999, 2002):
    for mo in range(1, 13):
        d = date(yr, mo, 1)
        x = date_to_x(d)
        lines.append(f'  <line x1="{x:.1f}" y1="{MARGIN_TOP}" x2="{x:.1f}" '
                     f'y2="{TOTAL_H - MARGIN_BOTTOM}" '
                     f'stroke="#e0ddd5" stroke-width="0.5"/>')

# ── レーンごとの水平線とラベル、点 ──
for i, cd in enumerate(CDS):
    cy = lane_cy(i)
    color = cd["color"]

    # 水平基準線
    lines.append(f'  <line x1="{MARGIN_LEFT}" y1="{cy:.1f}" '
                 f'x2="{MARGIN_LEFT + PLOT_W}" y2="{cy:.1f}" '
                 f'stroke="{color}" stroke-width="2" opacity="0.35"/>')

    # CD名ラベル
    lines.append(f'  <text x="{MARGIN_LEFT - 12}" y="{cy + 5:.1f}" '
                 f'text-anchor="end" font-size="14" font-weight="600" fill="{color}">'
                 f'{esc(cd["label"])}</text>')

    # 同じ日付に複数の点が重なる場合をオフセット
    date_count: dict[date, int] = defaultdict(int)
    for _, _, rel_date in cd["tracks"]:
        date_count[rel_date] += 1

    date_seen: dict[date, int] = defaultdict(int)
    for artist, title, rel_date in cd["tracks"]:
        x = date_to_x(rel_date)
        n = date_count[rel_date]
        idx = date_seen[rel_date]
        date_seen[rel_date] += 1

        # 重複がある場合は縦にオフセット
        if n > 1:
            spread = (n - 1) * 9
            offset_y = -spread / 2 + idx * 9
        else:
            offset_y = 0

        py = cy + offset_y
        tooltip = f"{esc(artist)} / {esc(title)} ({rel_date.strftime('%Y-%m-%d')})"

        lines.append(f'  <circle cx="{x:.1f}" cy="{py:.1f}" r="{R}" '
                     f'fill="{color}" opacity="0.85" stroke="white" stroke-width="1">'
                     f'<title>{tooltip}</title></circle>')

# ── タイトル ──
lines.append(f'  <text x="{MARGIN_LEFT}" y="28" font-size="16" font-weight="700" '
             f'fill="#3d3d3a">北青山的 — 収録曲の初出リリース年表</text>')

lines.append('</svg>')

svg_text = "\n".join(lines)

out_path = "/mnt/user-data/outputs/kita_aoyama_timeline.svg"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(svg_text)

print(f"Generated: {out_path}")
print(f"Size: {len(svg_text):,} bytes")

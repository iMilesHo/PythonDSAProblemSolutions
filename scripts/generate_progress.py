#!/usr/bin/env python3
"""
Generate LeetCode Top Interview 150 progress tracker SVG for README.

Reads problem data from resources/Top150Leetcode.json,
checks completed solutions in src/, and generates resources/progress.svg.

Usage:
    python3 generate_progress.py
"""

import json
import math
import os
from datetime import datetime
from pathlib import Path

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Paths
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "resources" / "Top150Leetcode.json"
SRC_DIR = ROOT / "src"
OUTPUT = ROOT / "resources" / "progress.svg"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Layout Constants
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SVG_W = 850
PAD = 25
COLS = 3
CARD_W, CARD_H = 250, 140
CARD_GAP = 20
CARD_R = 10
HEADER_H = 210
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Color Palette (GitHub / LeetCode dark theme)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLR = {
    "bg":      "#0d1117",
    "card":    "#161b22",
    "border":  "#30363d",
    "track":   "#21262d",
    "t1":      "#e6edf3",   # primary text
    "t2":      "#8b949e",   # secondary text
    "t3":      "#484f58",   # muted text
    "easy":    "#00b8a3",
    "med":     "#ffc01e",
    "hard":    "#ff375f",
    "bar_bg":  "#21262d",
    "sep":     "#30363d",
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SVG Helper Functions
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def esc(s):
    """Escape XML special characters."""
    return (str(s)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))


def svg_text(x, y, content, size=14, color=None, weight="normal", anchor="start"):
    """Generate an SVG <text> element."""
    c = color or CLR["t1"]
    return (
        f'<text x="{x}" y="{y}" fill="{c}" font-size="{size}" '
        f'font-weight="{weight}" font-family="{FONT}" '
        f'text-anchor="{anchor}">{esc(content)}</text>\n'
    )


def svg_ring(cx, cy, r, pct, stroke_w, track_color, fill_color):
    """Generate an SVG progress ring (track circle + progress arc)."""
    circ = 2 * math.pi * r
    s = (
        f'<circle cx="{cx}" cy="{cy}" r="{r}" '
        f'fill="none" stroke="{track_color}" stroke-width="{stroke_w}"/>\n'
    )
    if pct > 0:
        offset = circ * (1 - pct)
        s += (
            f'<circle cx="{cx}" cy="{cy}" r="{r}" '
            f'fill="none" stroke="{fill_color}" stroke-width="{stroke_w}" '
            f'stroke-linecap="round" '
            f'stroke-dasharray="{circ:.1f}" '
            f'stroke-dashoffset="{offset:.1f}" '
            f'transform="rotate(-90 {cx} {cy})"/>\n'
        )
    return s


def svg_bar(x, y, w, h, pct, color):
    """Generate an SVG horizontal progress bar."""
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2}" fill="{CLR["bar_bg"]}"/>\n'
    if pct > 0:
        filled = max(h, w * pct)
        s += f'<rect x="{x}" y="{y}" width="{filled:.1f}" height="{h}" rx="{h / 2}" fill="{color}"/>\n'
    return s


def progress_color(pct):
    """Return a color based on completion percentage."""
    if pct >= 0.75:
        return CLR["easy"]
    if pct >= 0.40:
        return CLR["med"]
    if pct > 0:
        return CLR["hard"]
    return CLR["t3"]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Data Parsing
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def get_solved_ids():
    """Extract solved LeetCode question IDs from src/ filenames.

    Filename pattern: {cat}_{idx}_{questionId}_{title}.py
    e.g. 01_04_0080_Remove_Duplicates_from_Sorted_Array_II.py → "80"
    """
    ids = set()
    if SRC_DIR.is_dir():
        for f in SRC_DIR.iterdir():
            if f.suffix == ".py":
                parts = f.stem.split("_")
                if len(parts) >= 3:
                    ids.add(parts[2].lstrip("0") or "0")
    return ids


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Main Generator
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def main():
    # Load problem data
    categories = json.loads(JSON_PATH.read_text())
    solved_ids = get_solved_ids()

    # ── Compute statistics per category ──
    cat_stats = []
    total_easy = total_med = total_hard = 0
    solved_easy = solved_med = solved_hard = 0

    for cat in categories:
        cs = {
            "name": cat["name"],
            "total": cat["questionNum"],
            "solved": 0,
            "e": [0, 0],  # [solved, total]
            "m": [0, 0],
            "h": [0, 0],
        }
        for q in cat["questions"]:
            diff = q["difficulty"]
            done = q["questionFrontendId"] in solved_ids

            if diff == "EASY":
                cs["e"][1] += 1; total_easy += 1
                if done:
                    cs["e"][0] += 1; solved_easy += 1; cs["solved"] += 1
            elif diff == "MEDIUM":
                cs["m"][1] += 1; total_med += 1
                if done:
                    cs["m"][0] += 1; solved_med += 1; cs["solved"] += 1
            else:
                cs["h"][1] += 1; total_hard += 1
                if done:
                    cs["h"][0] += 1; solved_hard += 1; cs["solved"] += 1

        cat_stats.append(cs)

    total_questions = sum(s["total"] for s in cat_stats)
    total_solved = solved_easy + solved_med + solved_hard
    overall_pct = total_solved / total_questions if total_questions else 0

    # ── Calculate SVG dimensions ──
    num_rows = math.ceil(len(cat_stats) / COLS)
    grid_x_offset = (SVG_W - (COLS * CARD_W + (COLS - 1) * CARD_GAP)) / 2
    grid_y = PAD + HEADER_H + 15
    grid_h = num_rows * CARD_H + (num_rows - 1) * CARD_GAP
    svg_h = grid_y + grid_h + PAD + 25  # 25 for footer

    # ── Build SVG ──
    svg = []
    svg.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{SVG_W}" height="{svg_h}" '
        f'viewBox="0 0 {SVG_W} {svg_h}">\n'
    )

    # Background
    svg.append(
        f'<rect width="{SVG_W}" height="{svg_h}" rx="16" fill="{CLR["bg"]}"/>\n'
    )

    # ━━━ HEADER SECTION ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    y0 = PAD

    # Title
    svg.append(svg_text(
        SVG_W / 2, y0 + 30,
        "LeetCode Top Interview 150",
        size=20, color=CLR["t1"], weight="700", anchor="middle"
    ))
    # Subtitle
    svg.append(svg_text(
        SVG_W / 2, y0 + 52,
        "Progress Dashboard",
        size=13, color=CLR["t2"], weight="400", anchor="middle"
    ))
    # Separator line
    svg.append(
        f'<line x1="{PAD + 20}" y1="{y0 + 68}" '
        f'x2="{SVG_W - PAD - 20}" y2="{y0 + 68}" '
        f'stroke="{CLR["sep"]}" stroke-width="1"/>\n'
    )

    # ── Overall progress ring (left side) ──
    ring_cx, ring_cy = 140, y0 + 140
    ring_r = 50
    svg.append(svg_ring(
        ring_cx, ring_cy, ring_r, overall_pct, 9,
        CLR["track"], progress_color(overall_pct)
    ))
    # Number inside ring
    svg.append(svg_text(
        ring_cx, ring_cy - 4, str(total_solved),
        size=28, color=CLR["t1"], weight="700", anchor="middle"
    ))
    svg.append(svg_text(
        ring_cx, ring_cy + 16, f"/ {total_questions}",
        size=12, color=CLR["t2"], weight="400", anchor="middle"
    ))
    svg.append(svg_text(
        ring_cx, ring_cy + 32, "Solved",
        size=10, color=CLR["t3"], weight="400", anchor="middle"
    ))

    # ── Difficulty breakdown bars (right side) ──
    bar_x = 260
    bar_w = 555
    bar_h = 8
    bar_spacing = 38
    diffs = [
        ("Easy",   solved_easy, total_easy, CLR["easy"]),
        ("Medium", solved_med,  total_med,  CLR["med"]),
        ("Hard",   solved_hard, total_hard, CLR["hard"]),
    ]
    for i, (label, s, t, color) in enumerate(diffs):
        by = y0 + 100 + i * bar_spacing
        pct = s / t if t else 0
        # Label
        svg.append(svg_text(bar_x, by, label, size=13, color=color, weight="600"))
        # Count
        svg.append(svg_text(
            bar_x + bar_w, by, f"{s} / {t}",
            size=13, color=CLR["t2"], weight="400", anchor="end"
        ))
        # Bar
        svg.append(svg_bar(bar_x, by + 8, bar_w, bar_h, pct, color))

    # ━━━ CATEGORY GRID ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    for idx, cs in enumerate(cat_stats):
        row, col = divmod(idx, COLS)
        cx = grid_x_offset + col * (CARD_W + CARD_GAP)
        cy = grid_y + row * (CARD_H + CARD_GAP)
        pct = cs["solved"] / cs["total"] if cs["total"] else 0
        color = progress_color(pct)

        # Card background
        svg.append(
            f'<rect x="{cx}" y="{cy}" width="{CARD_W}" height="{CARD_H}" '
            f'rx="{CARD_R}" fill="{CLR["card"]}" '
            f'stroke="{CLR["border"]}" stroke-width="1"/>\n'
        )

        # Category name
        svg.append(svg_text(
            cx + CARD_W / 2, cy + 22, cs["name"],
            size=12, color=CLR["t1"], weight="600", anchor="middle"
        ))

        # Progress ring
        rx, ry = cx + CARD_W / 2, cy + 68
        svg.append(svg_ring(rx, ry, 26, pct, 5, CLR["track"], color))

        # Ring text
        svg.append(svg_text(
            rx, ry - 1, f'{cs["solved"]}/{cs["total"]}',
            size=13, color=CLR["t1"], weight="700", anchor="middle"
        ))
        pct_label = f"{pct * 100:.0f}%"
        svg.append(svg_text(
            rx, ry + 13, pct_label,
            size=10, color=CLR["t2"], weight="400", anchor="middle"
        ))

        # Difficulty dots at card bottom
        dot_y = cy + CARD_H - 16
        dot_items = [
            (cs["e"][0], cs["e"][1], CLR["easy"]),
            (cs["m"][0], cs["m"][1], CLR["med"]),
            (cs["h"][0], cs["h"][1], CLR["hard"]),
        ]
        visible = [(sv, tv, co) for sv, tv, co in dot_items if tv > 0]
        if visible:
            item_w = 48
            start_x = cx + (CARD_W - len(visible) * item_w) / 2
            for j, (sv, tv, co) in enumerate(visible):
                ix = start_x + j * item_w
                svg.append(
                    f'<circle cx="{ix + 5}" cy="{dot_y}" r="3.5" fill="{co}"/>\n'
                )
                svg.append(svg_text(
                    ix + 12, dot_y + 4, f"{sv}/{tv}",
                    size=10, color=CLR["t2"]
                ))

    # ━━━ FOOTER ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    now = datetime.now().strftime("%Y-%m-%d")
    svg.append(svg_text(
        SVG_W / 2, svg_h - PAD,
        f"Last updated: {now}",
        size=10, color=CLR["t3"], weight="400", anchor="middle"
    ))

    svg.append("</svg>")

    # ── Write output ──
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("".join(svg))

    print(f"✅ Generated: {OUTPUT}")
    print(f"   {total_solved}/{total_questions} solved ({overall_pct * 100:.1f}%)")
    print(f"   Easy: {solved_easy}/{total_easy}  |  Medium: {solved_med}/{total_med}  |  Hard: {solved_hard}/{total_hard}")


if __name__ == "__main__":
    main()

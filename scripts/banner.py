#!/usr/bin/env python3
"""Render the README banner: the Orion mark at the heart of a spiral nebula.

Writes assets/banner.svg (brand colors, twinkling stars). Needs Pillow and the mark at assets/orion-star.png.

    python3 scripts/banner.py
"""
import math
import random
from pathlib import Path
from xml.etree import ElementTree

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
W, H = 80, 36          # grid in characters; cells are ~1:2, so this is near square
MARK_W = 40            # mark width in columns
SEED = 11

# Brand palette, from the Orion style sheet.
BG = "#101113"
INK = "#fafafa"
TEAL = (0x3C, 0xC5, 0xD2)
PURPLE = (0xD0, 0x73, 0xFA)
ORANGE = (0xFF, 0x89, 0x0B)
YELLOW = "#f5e94a"

# Quadrant blocks indexed by (top-left, top-right, bottom-left, bottom-right) bits.
QUADS = " \u2597\u2596\u2584\u259d\u2590\u259e\u259f\u2598\u259a\u258c\u2599\u2580\u259c\u259b\u2588"
RAMP = " .`':-~=+*%&"       # nebula density, thin to thick


def mark_mask():
    src = Image.open(ROOT / "assets/orion-star.png").convert("RGBA")
    img = Image.new("RGBA", src.size, "white")
    img.alpha_composite(src)
    img = img.convert("L")
    rows = round(MARK_W * img.height / img.width / 2)
    # Sample 2x2 subpixels per cell and draw each cell with a quadrant block.
    small = img.resize((MARK_W * 2, rows * 2), Image.LANCZOS)
    px = small.load()
    on = lambda x, y: px[x, y] < 128
    cells = []
    for y in range(rows):
        row = []
        for x in range(MARK_W):
            bits = (on(2 * x, 2 * y) << 3 | on(2 * x + 1, 2 * y) << 2
                    | on(2 * x, 2 * y + 1) << 1 | on(2 * x + 1, 2 * y + 1))
            row.append(QUADS[bits])
        cells.append(row)
    return cells


def noise(x, y, rnd):
    # Cheap value noise: a few octaves of hashed lattice points, smoothly blended.
    total, amp, freq = 0.0, 1.0, 0.09
    for octave in range(4):
        xi, yi = x * freq, y * freq
        x0, y0 = math.floor(xi), math.floor(yi)
        fx, fy = xi - x0, yi - y0
        fx, fy = fx * fx * (3 - 2 * fx), fy * fy * (3 - 2 * fy)

        def h(i, j):
            return rnd[(i * 73856093 ^ j * 19349663 ^ octave * 83492791) % len(rnd)]

        top = h(x0, y0) * (1 - fx) + h(x0 + 1, y0) * fx
        bot = h(x0, y0 + 1) * (1 - fx) + h(x0 + 1, y0 + 1) * fx
        total += amp * (top * (1 - fy) + bot * fy)
        amp, freq = amp / 2, freq * 2
    return total / 1.875


def mix(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def hexcolor(c, alpha=1.0):
    c = tuple(round(v * alpha) for v in c)   # fade toward black background
    return "#%02x%02x%02x" % c


def build():
    random.seed(SEED)
    rnd = [random.random() for _ in range(4096)]
    mask = mark_mask()
    mh = len(mask)
    ox, oy = (W - MARK_W) // 2, (H - mh) // 2
    cx, cy = W / 2 - 0.5, H / 2 - 0.5

    grid = [[(" ", None, False) for _ in range(W)] for _ in range(H)]
    for y in range(H):
        for x in range(W):
            dx, dy = (x - cx) / (W / 2), (y - cy) * 2 / (W / 2)
            r = math.hypot(dx, dy)
            theta = math.atan2(dy, dx)
            # Four logarithmic arms, one per hook of the mark, turning the same way.
            arm = 0.0
            for k in range(4):
                phase = theta - k * math.pi / 2 - 1.7 * math.log(r + 0.08)
                arm = max(arm, math.cos(phase) ** 2 if math.cos(phase) > 0 else 0)
            falloff = math.exp(-((r - 0.7) ** 2) / 0.06)
            falloff *= min(1.0, max(0.0, (r - 0.54) / 0.12))   # dark core for the mark
            n = noise(x, y * 2, rnd)
            d = (0.9 * arm ** 4 + 0.55 * n - 0.42) * falloff
            d = max(0.0, min(0.999, d * 2.1))
            ch = RAMP[int(d * len(RAMP))]
            if ch != " ":
                # Teal near the core, purple through the arms, orange at the rim.
                t = min(1.0, max(0.0, (r - 0.55) / 0.5))
                col = mix(TEAL, PURPLE, t / 0.55) if t < 0.55 else mix(PURPLE, ORANGE, (t - 0.55) / 0.45)
                grid[y][x] = (ch, hexcolor(col, 0.55 + 0.45 * d), False)
            elif r > 0.56 and rnd[(x * 31 + y * 97) % 4096] < 0.035:
                star = "*" if rnd[(x * 7 + y * 13) % 4096] < 0.3 else "+" if rnd[(x * 5 + y) % 4096] < 0.5 else "."
                grid[y][x] = (star, YELLOW if star == "*" else INK, star != ".")

    # Clear a soft halo around the mark, then stamp it.
    for y in range(mh):
        for x in range(MARK_W):
            if mask[y][x] != " ":
                for j in (-1, 0, 1):
                    for i in (-1, 0, 1):
                        gy, gx = oy + y + j, ox + x + i
                        if 0 <= gy < H and 0 <= gx < W:
                            grid[gy][gx] = (" ", None, False)
    for y in range(mh):
        for x in range(MARK_W):
            if mask[y][x] != " ":
                grid[oy + y][ox + x] = (mask[y][x], INK, False)

    # A single bright point in the mark's empty center.
    ccx, ccy = round(cx), round(cy)
    grid[ccy][ccx] = ("*", YELLOW, True)
    return grid


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def write_svg(grid):
    cw, lh, pad = 9.6, 18, 36
    width = round(W * cw + pad * 2)
    art_h = H * lh
    height = art_h + pad * 2 + 70
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="Orion examples">',
        "<style>",
        "text{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:16px;white-space:pre}",
        ".w{font-family:Aspekta,Inter,'Helvetica Neue',Arial,sans-serif;white-space:normal}",
        "@keyframes tw{0%,100%{opacity:1}50%{opacity:.15}}",
        ".t{animation:tw 3.2s ease-in-out infinite}",
        "@media (prefers-reduced-motion:reduce){.t{animation:none}}",
        "</style>",
        "<defs>",
        f'<radialGradient id="core"><stop offset="0" stop-color="{hexcolor(TEAL)}" stop-opacity=".22"/>'
        f'<stop offset="1" stop-color="{hexcolor(TEAL)}" stop-opacity="0"/></radialGradient>',
        f'<radialGradient id="haze"><stop offset=".45" stop-color="{hexcolor(PURPLE)}" stop-opacity="0"/>'
        f'<stop offset=".7" stop-color="{hexcolor(PURPLE)}" stop-opacity=".10"/>'
        f'<stop offset="1" stop-color="{hexcolor(ORANGE)}" stop-opacity="0"/></radialGradient>',
        "</defs>",
        f'<rect width="{width}" height="{height}" rx="16" fill="{BG}"/>',
        f'<circle cx="{width / 2}" cy="{pad + art_h / 2}" r="{art_h * 0.55}" fill="url(#haze)"/>',
        f'<circle cx="{width / 2}" cy="{pad + art_h / 2}" r="{art_h * 0.3}" fill="url(#core)"/>',
    ]
    twinkle = 0
    for y, row in enumerate(grid):
        by = pad + (y + 1) * lh - 4
        x = 0
        while x < W:
            ch, col, tw = row[x]
            if ch == " " or ch in QUADS:
                x += 1
                continue
            if tw:
                delay = (twinkle * 0.73) % 3.2
                twinkle += 1
                out.append(f'<text x="{pad + x * cw:.1f}" y="{by}" fill="{col}" class="t" '
                           f'style="animation-delay:{delay:.2f}s">{esc(ch)}</text>')
                x += 1
                continue
            run = ch
            while x + len(run) < W and row[x + len(run)][1] == col and not row[x + len(run)][2] \
                    and row[x + len(run)][0] != " ":
                run += row[x + len(run)][0]
            out.append(f'<text x="{pad + x * cw:.1f}" y="{by}" fill="{col}">{esc(run)}</text>')
            x += len(run)
    # The mark as crisp pixels: one rect per run of filled quadrants.
    sub_w, sub_h = cw / 2, lh / 2
    for y, row in enumerate(grid):
        for half in (0, 1):
            subs = []
            for x, (ch, _, _) in enumerate(row):
                bits = QUADS.index(ch) if ch in QUADS and ch != " " else 0
                subs += [bool(bits >> (3 - 2 * half) & 1), bool(bits >> (2 - 2 * half) & 1)]
            i = 0
            while i < len(subs):
                if not subs[i]:
                    i += 1
                    continue
                j = i
                while j < len(subs) and subs[j]:
                    j += 1
                out.append(f'<rect x="{pad + i * sub_w:.1f}" y="{pad + y * lh + half * sub_h:.1f}" '
                           f'width="{(j - i) * sub_w + 0.3:.1f}" height="{sub_h + 0.3:.1f}" fill="{INK}"/>')
                i = j
    wy = pad + art_h + 44
    out.append(f'<text class="w" x="{width / 2}" y="{wy}" text-anchor="middle" fill="{INK}" '
               f'style="font-size:34px;font-weight:600;letter-spacing:-0.5px">Orion</text>')
    out.append(f'<text class="w" x="{width / 2}" y="{wy + 28}" text-anchor="middle" '
               f'fill="{hexcolor(TEAL)}" style="font-size:13px;font-weight:600;letter-spacing:4.5px">EXAMPLES</text>')
    out.append("</svg>")
    svg = "\n".join(out) + "\n"
    ElementTree.fromstring(svg)   # fail here rather than ship a broken banner
    (ROOT / "assets/banner.svg").write_text(svg)


if __name__ == "__main__":
    write_svg(build())

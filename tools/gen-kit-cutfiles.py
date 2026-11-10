#!/usr/bin/env python3
"""Generate the Katha 01 (Chanakya) kit cut files as SVG, 1 unit = 1 mm.

Run:  python3 tools/gen-kit-cutfiles.py
Out:  katha/assets/kit/*.svg

Layers (by stroke colour):
  red   = cut through
  green = fold / score
  blue  = raised ridge or line on the stencil BASE PLATE (not cut in the frame)
  black = etched or printed label / guide, never cut
"""
import math
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "katha", "assets", "kit")
T = 3.0          # greyboard thickness for the phone stand (slot width)
CUT = 'fill="none" stroke="#e00000" stroke-width="0.2"'
FOLD = 'fill="none" stroke="#00a040" stroke-width="0.2" stroke-dasharray="2 1"'
RIDGE = 'fill="none" stroke="#0050d0" stroke-width="2.5" stroke-linecap="round"'
LINE = 'fill="none" stroke="#0050d0" stroke-width="0.6" stroke-linecap="round"'
ETCH = 'fill="none" stroke="#000" stroke-width="0.15"'


def f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def poly(pts, r=0.0, style=CUT):
    """Closed polygon; r > 0 rounds every corner."""
    n = len(pts)
    if r <= 0:
        d = "M" + " L".join(f"{f(x)},{f(y)}" for x, y in pts) + " Z"
        return f'<path d="{d}" {style}/>'
    d = []
    for i in range(n):
        p0, p1, p2 = pts[i - 1], pts[i], pts[(i + 1) % n]
        def toward(a, b):
            L = math.hypot(b[0] - a[0], b[1] - a[1])
            k = min(r, L / 2) / L
            return (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)
        a, b = toward(p1, p0), toward(p1, p2)
        d.append(("M" if i == 0 else "L") + f"{f(a[0])},{f(a[1])} Q{f(p1[0])},{f(p1[1])} {f(b[0])},{f(b[1])}")
    return f'<path d="{" ".join(d)} Z" {style}/>'


def rect(x, y, w, h, r=0.0, style=CUT):
    return f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{f(r)}" {style}/>'


def circle(x, y, d, style=CUT):
    return f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(d / 2)}" {style}/>'


def line(x1, y1, x2, y2, style=FOLD):
    return f'<path d="M{f(x1)},{f(y1)} L{f(x2)},{f(y2)}" {style}/>'


def text(x, y, s, size=3.0, anchor="start"):
    return (f'<text x="{f(x)}" y="{f(y)}" font-family="Arial, sans-serif" font-size="{f(size)}" '
            f'text-anchor="{anchor}" fill="#000">{s}</text>')


def save(name, w, h, body):
    os.makedirs(OUT, exist_ok=True)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{f(w)}mm" height="{f(h)}mm" '
           f'viewBox="0 0 {f(w)} {f(h)}">\n' + "\n".join(body) + "\n</svg>\n")
    with open(os.path.join(OUT, name), "w") as fh:
        fh.write(svg)
    print("wrote", name, f"{f(w)} x {f(h)} mm")


# ---------------------------------------------------------------- stencils
SW, SH = 180.0, 120.0   # every stencil sheet


def sheet(title):
    return [rect(0, 0, SW, SH, 4), text(SW - 6, SH - 5, title, 3.2, "end")]


def taper_v(x, y, w_top, w_bot, L, n):
    """Vertical tapered wrap, top-left of bounding box at (x, y)."""
    wmax = max(w_top, w_bot)
    cx = x + wmax / 2
    pts = [(cx - w_top / 2, y), (cx + w_top / 2, y), (cx + w_bot / 2, y + L), (cx - w_bot / 2, y + L)]
    return [poly(pts, 3), line(cx, y + 5, cx, y + L - 5, RIDGE), text(cx, y + L + 4.5, str(n), 3, "middle")]


def taper_h(x, y, w_a, w_b, L, n):
    """Horizontal tapered wrap."""
    wmax = max(w_a, w_b)
    cy = y + wmax / 2
    pts = [(x, cy - w_a / 2), (x + L, cy - w_b / 2), (x + L, cy + w_b / 2), (x, cy + w_a / 2)]
    return [poly(pts, 3), line(x + 5, cy, x + L - 5, cy, RIDGE), text(x + L + 2, cy + 1, str(n), 3)]


def stencil_body():
    b = sheet("KATHA 01 · STENCIL 1 · BODY")
    # legs: finished 13 mm thigh -> 10 mm ankle around the wire, 3 mm sheet
    b += taper_v(8, 8, 31, 22, 65, 1)
    b += taper_v(47, 8, 31, 22, 65, 1)
    # torso front and back (back carries the spine groove)
    for i, x in enumerate((86, 128)):
        pts = [(x, 8), (x + 34, 8), (x + 32, 58), (x + 28, 70), (x + 6, 70), (x + 2, 58)]
        b.append(poly(pts, 4))
        b.append(text(x + 17, 76.5, "2 front" if i == 0 else "2 back", 3, "middle"))
        if i == 1:
            b.append(line(x + 17, 13, x + 17, 65, RIDGE))
    # arms: finished 10 mm shoulder -> 8 mm wrist
    b += taper_h(8, 88, 22, 16, 65, 3)
    b += taper_h(88, 88, 22, 16, 65, 3)
    save("stencil-1-body.svg", SW, SH, b)


def peanut(x, y, L, lobe, waist):
    R, d = lobe / 2, L / 2 - lobe / 2
    top, bot = [], []
    N = 60
    for i in range(N + 1):
        u = -L / 2 + L * i / N
        a = abs(u)
        h = waist / 2 + (R - waist / 2) * (a / d) ** 2 if a <= d else math.sqrt(max(R * R - (a - d) ** 2, 0))
        top.append((x + L / 2 + u, y + R - h))
        bot.append((x + L / 2 + u, y + R + h))
    return poly(top + bot[::-1])


def stencil_head():
    b = sheet("KATHA 01 · STENCIL 2 · HEAD, HANDS, FEET")
    # head: two peanut pieces close around a 24 mm foil ball -> 30 mm head
    for x in (8, 72):
        b.append(peanut(x, 8, 56, 23.5, 10.5))
        b.append(text(x + 28, 37, "4 head half", 3, "middle"))
    for x in (140, 154):                                   # ears
        b.append(rect(x, 10, 6, 9, 3))
    b.append(text(150, 24.5, "5 ears", 3, "middle"))
    mitt = [(2, 20), (0, 8), (1, 2), (5, 0), (9, 1), (10, 6), (13, 5), (14, 9), (11, 13), (10, 20)]
    for i, x in enumerate((8, 28, 48, 68)):                # hands, 2 per hand
        pts = [(x + (14 - px if i % 2 else px), 46 + py) for px, py in mitt]
        b.append(poly(pts, 1.5))
    b.append(text(45, 72, "6 hands (2 pieces sandwich each hand loop)", 3, "middle"))
    for x in (96, 116, 136, 156):                          # feet, 2 per foot
        b.append(rect(x, 46, 14, 26, 6.5))
    b.append(text(133, 78, "7 feet (2 pieces sandwich each foot loop)", 3, "middle"))
    save("stencil-2-head-hands-feet.svg", SW, SH, b)


def stencil_chanakya():
    b = sheet("KATHA 01 · STENCIL 3 · CHANAKYA")
    # dhoti: wraps hips (66 mm) flaring to 90 mm, pleat lines pressed in by the base plate
    x, y = 8, 8
    b.append(poly([(x + 12, y), (x + 78, y), (x + 90, y + 55), (x, y + 55)], 3))
    for i in range(1, 6):
        xt, xb = x + 12 + 66 * i / 6, x + 90 * i / 6
        b.append(line(xt, y + 6, xb, y + 50, LINE))
    b.append(text(x + 45, y + 60.5, "8 dhoti (lines = pleats)", 3, "middle"))
    b.append(rect(8, 76, 100, 3, 1.5))                     # sacred thread
    b.append(text(58, 84.5, "9 sacred thread", 3, "middle"))
    cx, cy = 122, 22                                       # shikha
    tear = [(0, -12), (4, -2), (5, 3), (3.5, 7.5), (0, 9), (-3.5, 7.5), (-5, 3), (-4, -2)]
    b.append(poly([(cx + px, cy + py) for px, py in tear], 2))
    b.append(text(cx, 37, "10 shikha", 3, "middle"))
    for x in (140, 154):                                   # eyebrows
        b.append(rect(x, 14, 10, 3, 1.4))
    b.append(text(152, 23, "11 brows", 3, "middle"))
    mx, my = 152, 34                                       # moustache
    mou = [(-9, 0), (-5, -2.5), (0, -1), (5, -2.5), (9, 0), (5, 2.5), (0, 1.5), (-5, 2.5)]
    b.append(poly([(mx + px, my + py) for px, py in mou], 1))
    b.append(text(mx, 42.5, "12 moustache", 3, "middle"))
    save("stencil-3-chanakya.svg", SW, SH, b)


# ------------------------------------------------------------- phone stand
# Side rib, local coords: x forward->back, y up. Phone foot goes in one of four
# notches; its back leans on the top bar. Notch choice sets the angle.
FLOOR, LIP = 12.0, 6.0
NOTCHES = [(69, 82, "80°"), (51, 64, "70°"), (31, 44, "60°"), (6, 19, "50°")]   # (front, rear, lean)
BAR_X, RIB_TOP, BAR_TOP = 99.0, 85.0, 107.0


def rib_points():
    p = [(0, 0), (0, FLOOR + LIP)]
    for front, rear, _ in sorted(NOTCHES):
        p += [(front, FLOOR + LIP), (front, FLOOR), (rear, FLOOR), (rear, FLOOR + LIP)]
    p.pop()                                   # no tooth behind the last notch
    p += [(90, FLOOR + LIP), (95.5, RIB_TOP),
          (BAR_X, RIB_TOP), (BAR_X, RIB_TOP - 12), (BAR_X + T, RIB_TOP - 12), (BAR_X + T, RIB_TOP),   # top-bar slot
          (112, RIB_TOP), (140, 0),
          (123, 0), (123, 15), (120, 15), (120, 0),                                                    # rear spreader slot
          (25, 0), (25, 9), (22, 9), (22, 0)]                                                          # front spreader slot
    return p


def bar(x, y, w, h, slot, from_top, label):
    """Cross bar with two half-lap slots centred 23.5 mm either side of centre."""
    c = x + w / 2
    xs = [c - 23.5 - T / 2, c - 23.5 + T / 2, c + 23.5 - T / 2, c + 23.5 + T / 2]
    if from_top:
        pts = [(x, y), (xs[0], y), (xs[0], y + slot), (xs[1], y + slot), (xs[1], y),
               (xs[2], y), (xs[2], y + slot), (xs[3], y + slot), (xs[3], y), (x + w, y), (x + w, y + h), (x, y + h)]
    else:
        pts = [(x, y), (x + w, y), (x + w, y + h), (xs[3], y + h), (xs[3], y + h - slot), (xs[2], y + h - slot),
               (xs[2], y + h), (xs[1], y + h), (xs[1], y + h - slot), (xs[0], y + h - slot), (xs[0], y + h), (x, y + h)]
    return [poly(pts), text(c, y + (h / 2 + 4 if from_top else h / 2), label, 2.8, "middle")]


def insert_phone_stand():
    W, H = 246.0, 166.0
    b = [rect(0, 0, W, H, 2), text(W - 6, H - 4, "KATHA 01 · INSERT · PHONE STAND · 3 mm greyboard", 3, "end")]
    rp = rib_points()
    b.append(poly([(8 + x, 160 - y) for x, y in rp]))                 # rib A, upright
    b.append(poly([(150 - x, 8 + y) for x, y in rp]))                 # rib B, rotated 180 to nest
    for front, rear, lean in NOTCHES:
        b.append(text(8 + (front + rear) / 2, 160 - 3.5, lean, 2.6, "middle"))
        b.append(text(150 - (front + rear) / 2, 8 + 6, lean, 2.6, "middle"))
    b.append(text(8 + 112, 160 - 30, "A", 5, "middle"))
    b.append(text(150 - 112, 8 + 34, "B", 5, "middle"))
    b += bar(166, 8, 70, 34, 12, False, "TOP BAR")
    b += bar(166, 52, 70, 30, 15, True, "REAR")
    b += bar(166, 92, 70, 18, 9, True, "FRONT")
    save("insert-phone-stand.svg", W, H, b)


# --------------------------------------------------------------------- box
BL, BW, BD = 250.0, 170.0, 45.0     # tray inside: length, width, depth


def tray_stage():
    m = 8.0
    W, H = BL + 2 * BD + 2 * m, BW + 2 * BD + 2 * m
    x0, y0 = m + BD, m + BD
    tab = 30.0
    outline = [
        (x0, y0), (x0, y0 - BD), (x0 + BL, y0 - BD), (x0 + BL, y0),                       # rear long wall
        (x0 + BL + BD, y0), (x0 + BL + BD, y0 + BW), (x0 + BL, y0 + BW),                  # right short wall
        (x0 + BL, y0 + BW + BD), (x0, y0 + BW + BD), (x0, y0 + BW),                       # front long wall
        (x0 - BD, y0 + BW), (x0 - BD, y0),                                                # left short wall
    ]
    b = [poly(outline)]
    # corner tabs on the long walls (fold in, tuck or glue behind the short walls)
    for yy, s in ((y0, -1), (y0 + BW, 1)):
        for xx, d in ((x0, -1), (x0 + BL, 1)):
            b.append(poly([(xx, yy + s * 1.5), (xx + d * tab, yy + s * 5), (xx + d * tab, yy + s * (BD - 5)), (xx, yy + s * (BD - 1.5))]))
            b.append(line(xx, yy + s * 1.5, xx, yy + s * (BD - 1.5)))
    b += [line(x0, y0, x0 + BL, y0), line(x0, y0 + BW, x0 + BL, y0 + BW),
          line(x0, y0, x0, y0 + BW), line(x0 + BL, y0, x0 + BL, y0 + BW)]
    # peg holes: 5.2 mm on a 20 mm grid; the tray flipped over is the stage floor
    for i in range(9):
        for j in range(5):
            b.append(circle(x0 + 45 + 20 * i, y0 + 55 + 20 * j, 5.2))
    # slits for the backdrop tabs, 12 mm in from the rear edge
    for xs in (40, 170):
        b.append(rect(x0 + xs, y0 + 12, 40.6, 1.8))
    b.append(text(x0 + BL / 2, y0 + 30, "REAR · backdrop tabs go in the two slits", 3.2, "middle"))
    b.append(text(x0 + BL / 2, y0 + BW - 8, "KATHA 01 · TRAY = STAGE (flip over) · 250 x 170 x 45 inside · 1.5 mm board", 3.2, "middle"))
    save("box-tray-stage.svg", W, H, b)


def backdrop():
    W, H = 250.0, 250.0
    pts = [(0, 0), (W, 0), (W, 235), (210, 235), (210, 250), (170, 250), (170, 235),
           (80, 235), (80, 250), (40, 250), (40, 235), (0, 235)]
    b = [poly(pts), line(0, 85, W, 85)]
    # stepped torana arch, print guide only
    arch = [(45, 235), (45, 110), (60, 110), (60, 85), (80, 85), (80, 62), (105, 62), (105, 45),
            (145, 45), (145, 62), (170, 62), (170, 85), (190, 85), (190, 110), (205, 110), (205, 235)]
    b.append('<path d="M' + " L".join(f"{f(x)},{f(y)}" for x, y in arch) + f'" {ETCH}/>')
    b.append(text(125, 78, "fold here to store (85 + 165 mm)", 3.2, "middle"))
    b.append(text(125, 228, "KATHA 01 · BACKDROP · arch is a print guide, not a cut", 3.2, "middle"))
    save("backdrop.svg", W, H, b)


def sleeve_display():
    # slipcase around the tray; stood on end it is the display box (window + acrylic)
    L, Wd, D = 256.0, 175.0, 48.5      # inside length, width, depth
    m, glue, flap = 8.0, 15.0, 40.0
    W = 2 * Wd + 2 * D + glue + 2 * m
    H = L + D + 15 + 2 * m
    x, y = m, m
    xs = [x, x + Wd, x + Wd + D, x + 2 * Wd + D, x + 2 * Wd + 2 * D]      # back | side | front | side | glue
    out = [(xs[0], y), (xs[4], y), (xs[4] + glue, y + 6), (xs[4] + glue, y + L - 6), (xs[4], y + L),
           (xs[4] - 3, y + L + flap), (xs[3] + 3, y + L + flap), (xs[3], y + L),                       # dust flap
           (xs[3], y + L + D), (xs[3] - 4, y + L + D + 15), (xs[2] + 4, y + L + D + 15), (xs[2], y + L + D), (xs[2], y + L),  # bottom + tuck
           (xs[2] - 3, y + L + flap), (xs[1] + 3, y + L + flap), (xs[1], y + L),                       # dust flap
           (xs[0], y + L)]
    b = [poly(out)]
    for xv in xs[1:]:
        b.append(line(xv, y, xv, y + L))
    b += [line(xs[1], y + L, xs[4], y + L), line(xs[2], y + L + D, xs[3], y + L + D)]
    # window on the front panel, 140 x 215; acrylic 155 x 230 sits behind it
    wx, wy = xs[2] + (Wd - 140) / 2, y + 18
    b.append(rect(wx, wy, 140, 215, 6))
    b.append(rect(wx - 7.5, wy - 7.5, 155, 230, 0, ETCH))
    b.append(text(xs[2] + Wd / 2, wy + 222, "FRONT · window 140 x 215 · acrylic 155 x 230 behind", 3.2, "middle"))
    b.append(text(xs[0] + Wd / 2, y + L / 2, "BACK", 5, "middle"))
    b.append(text(xs[0] + Wd / 2, y + L / 2 + 8, "KATHA 01 · SLEEVE = DISPLAY BOX · 256 x 175 x 48.5 inside", 3.2, "middle"))
    b.append(text(xs[4] + glue / 2, y + L / 2, "glue", 2.8, "middle"))
    save("box-sleeve-display.svg", W, H, b)


if __name__ == "__main__":
    stencil_body()
    stencil_head()
    stencil_chanakya()
    insert_phone_stand()
    tray_stage()
    backdrop()
    sleeve_display()

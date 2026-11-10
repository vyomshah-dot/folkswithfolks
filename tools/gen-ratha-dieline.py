#!/usr/bin/env python3
"""Katha 01 · Chanakya ratha box — dieline set with artwork.

Run:  python3 tools/gen-ratha-dieline.py
Out:  katha/assets/kit/ratha/page-*.svg and Katha01-Ratha-Dieline.pdf

Every page is drawn at 1:1, 1 SVG unit = 1 mm.
Dieline layers (drawn over the artwork):
  red solid      = cut
  green dashed   = fold (crease)
  green dotted   = light score (roof band, helps it curve)
  blue           = glue area
"""
import math
import os
import subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "katha", "assets", "kit", "ratha")
FONTS = os.path.join(ROOT, "brand-core", "fonts")

TERRA, MARI, INDIGO = "#C24E3A", "#E8A33D", "#2E3A59"
PAPER, DEEP, INK, CARD, NEEM = "#F4ECDD", "#EADDC6", "#2A241F", "#FBF6EB", "#5C7A4A"
KRAFT = "#D8C3A5"

CUT = 'fill="none" stroke="#E4002B" stroke-width="0.4" stroke-linejoin="round"'
FOLD = 'fill="none" stroke="#00A651" stroke-width="0.4" stroke-dasharray="3 1.6"'
SCORE = 'fill="none" stroke="#00A651" stroke-width="0.3" stroke-dasharray="0.8 1.6"'
GLUE = 'fill="#3B82F6" fill-opacity="0.18" stroke="none"'

DISPLAY, STORY, BODY = "Bricolage Grotesque", "Fraunces", "Hanken Grotesk"


def f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def pts(p):
    return " ".join(f"{f(x)},{f(y)}" for x, y in p)


def poly(p, style=CUT, closed=True):
    return f'<path d="M{pts(p)}{" Z" if closed else ""}" {style}/>'


def fillpoly(p, fill, extra=""):
    return f'<path d="M{pts(p)} Z" fill="{fill}" {extra}/>'


def line(x1, y1, x2, y2, style=FOLD):
    return f'<path d="M{f(x1)},{f(y1)} L{f(x2)},{f(y2)}" {style}/>'


def rect(x, y, w, h, fill="none", extra=""):
    return f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{fill}" {extra}/>'


def circ(cx, cy, r, fill="none", extra=""):
    return f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{fill}" {extra}/>'


def text(x, y, s, size, fill=INK, family=BODY, weight=400, anchor="start", italic=False, ls=0, extra=""):
    st = ' font-style="italic"' if italic else ""
    lsa = f' letter-spacing="{f(ls)}"' if ls else ""
    return (f'<text x="{f(x)}" y="{f(y)}" font-family="{family}" font-size="{f(size)}" font-weight="{weight}"'
            f' fill="{fill}" text-anchor="{anchor}"{st}{lsa} {extra}>{s}</text>')


def arc_pts(cx, cy, r, a0, a1, n=48):
    """Points on a circle in SVG coords (y down); angles in degrees, 0 = +x, 90 = up."""
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
             cy - r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


def chaitya_pts(cx, bottom, legtop, a, R, n=60):
    """Horseshoe (chaitya) arch outline, SVG coords. Legs at cx±a from bottom up to legtop."""
    k = math.sqrt(R * R - a * a)
    cy = legtop - k                     # circle centre sits above the leg tops
    phi = math.degrees(math.asin(k / R))
    arc = arc_pts(cx, cy, R, 180 + phi, -phi, n)     # left leg top, over the top, to right leg top
    return [(cx - a, bottom)] + arc + [(cx + a, bottom)]


# ------------------------------------------------------------------ motifs
def lotus(cx, cy, s, fill, edge=None, sw=0.06):
    petal = "M0,0 C-0.32,-0.3 -0.28,-0.8 0,-1 C0.28,-0.8 0.32,-0.3 0,0Z"
    st = f' stroke="{edge}" stroke-width="{sw}"' if edge else ""
    g = [f'<g transform="translate({f(cx)},{f(cy)}) scale({f(s)})">']
    for ang, sc in ((-64, .62), (64, .62), (-32, .86), (32, .86), (0, 1)):
        g.append(f'<path d="{petal}" transform="rotate({ang}) scale({sc})" fill="{fill}"{st}/>')
    g.append(f'<path d="M-0.62,0.03 Q0,0.34 0.62,0.03 Q0,0.13 -0.62,0.03Z" fill="{fill}"{st}/>')
    g.append("</g>")
    return "".join(g)


def wheel(cx, cy, r, ground, ink):
    g = [circ(cx, cy, r, ground),
         circ(cx, cy, r * 0.9, "none", f'stroke="{ink}" stroke-width="{f(r * 0.09)}"'),
         circ(cx, cy, r * 0.985, "none", f'stroke="{ink}" stroke-width="{f(r * 0.025)}"')]
    for i in range(16):
        a = math.radians(i * 22.5)
        g.append(line(cx + r * 0.24 * math.cos(a), cy + r * 0.24 * math.sin(a),
                      cx + r * 0.84 * math.cos(a), cy + r * 0.84 * math.sin(a),
                      f'stroke="{ink}" stroke-width="{f(r * 0.055)}" stroke-linecap="round"'))
    g.append(circ(cx, cy, r * 0.25, ink))
    g.append(lotus(cx, cy + r * 0.1, r * 0.2, ground))
    return "".join(g)


def sun(cx, cy, r, col):
    g = [circ(cx, cy, r * 0.42, col)]
    for i in range(8):
        a = math.radians(i * 45)
        g.append(line(cx + r * 0.6 * math.cos(a), cy + r * 0.6 * math.sin(a), cx + r * math.cos(a), cy + r * math.sin(a),
                      f'stroke="{col}" stroke-width="{f(r * 0.16)}" stroke-linecap="round"'))
    return "".join(g)


def coin(cx, cy, s, ground, ink):
    """Mauryan punch-marked coin: bent silver bar stamped with a sun and a six-armed sign."""
    w, h = s, s * 0.78
    body = [(cx - w / 2 + s * .06, cy - h / 2), (cx + w / 2, cy - h / 2 + s * .04), (cx + w / 2 - s * .03, cy + h / 2),
            (cx - w / 2, cy + h / 2 - s * .05)]
    g = [fillpoly(body, ground, f'stroke="{ink}" stroke-width="{f(s * .04)}" stroke-linejoin="round"'),
         sun(cx - s * .2, cy, s * .2, ink)]
    x6 = cx + s * .2
    g.append(circ(x6, cy, s * .05, ink))
    for i in range(6):
        a = math.radians(i * 60)
        g.append(line(x6, cy, x6 + s * .13 * math.cos(a), cy + s * .13 * math.sin(a),
                      f'stroke="{ink}" stroke-width="{f(s * .03)}"'))
        g.append(circ(x6 + s * .16 * math.cos(a), cy + s * .16 * math.sin(a), s * .03, ink))
    return "".join(g)


def palmleaf(x, y, w, h, ground, ink):
    g = [rect(x, y, w, h, ground, f'rx="{f(h / 2)}" stroke="{ink}" stroke-width="{f(h * .06)}"')]
    for fx in (.3, .7):
        g.append(circ(x + w * fx, y + h / 2, h * .1, ink))
    for i, fy in enumerate((.3, .5, .7)):
        for x0, x1 in ((.1, .26), (.34, .66), (.74, .9)):
            g.append(line(x + w * x0, y + h * fy, x + w * x1, y + h * fy,
                          f'stroke="{ink}" stroke-width="{f(h * .045)}" stroke-dasharray="{f(h * .12)} {f(h * .06)}"'))
    return "".join(g)


def pillar(x, top, w, h, col, acc):
    """Mauryan polished pillar with inverted-lotus bell capital. (x, top) = shaft's top-left."""
    ab, bell = h * .045, h * .09
    g = [rect(x - w * .45, top, w * 1.9, ab, col),
         fillpoly([(x - w * .15, top + ab), (x + w * 1.15, top + ab), (x + w * 1.35, top + ab + bell),
                   (x - w * .35, top + ab + bell)], col)]
    for i in range(1, 5):
        fx = i / 5
        g.append(line(x - w * .15 + w * 1.3 * fx, top + ab + 0.5, x - w * .35 + w * 1.7 * fx, top + ab + bell - 0.5,
                      f'stroke="{acc}" stroke-width="{f(w * .07)}"'))
    shaft_top = top + ab + bell
    g.append(rect(x, shaft_top, w, h - ab - bell - h * .03, col))
    g.append(line(x + w * .3, shaft_top + 2, x + w * .3, top + h * .95, f'stroke="{acc}" stroke-width="{f(w * .12)}" opacity=".7"'))
    g.append(rect(x - w * .2, top + h * .97, w * 1.4, h * .03, col))
    return "".join(g)


def lotus_band(x, y, w, h, ground, col, step=None):
    step = step or h * 1.25
    g = [rect(x, y, w, h, ground), line(x, y + h * .12, x + w, y + h * .12, f'stroke="{col}" stroke-width="{f(h * .05)}"'),
         line(x, y + h * .88, x + w, y + h * .88, f'stroke="{col}" stroke-width="{f(h * .05)}"')]
    n = int(w // step)
    off = (w - n * step) / 2 + step / 2
    for i in range(n):
        g.append(lotus(x + off + i * step, y + h * .74, h * .5, col))
    return "".join(g)


def page(name, title, w, h, body):
    W, H = w, h
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{f(W)}mm" height="{f(H)}mm" viewBox="0 0 {f(W)} {f(H)}">'
           f'{rect(0, 0, W, H, "#ffffff")}' + "".join(body) +
           text(14, H - 12, title, 9, INK, BODY, 500) +
           text(W - 14, H - 12, "Katha 01 · Chanakya ratha · 1:1 · mm · cut <tspan fill='#E4002B'>red</tspan> · fold "
                "<tspan fill='#00A651'>green dashed</tspan> · glue <tspan fill='#3B82F6'>blue</tspan>", 4.2, INK, BODY, 400, "end") +
           "</svg>")
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, name + ".svg")
    with open(p, "w") as fh:
        fh.write(svg)
    print("wrote", name, f"{f(W)} x {f(H)} mm")
    return p, W, H


# =============================================================== the box
L, BW, BH, GLUEW = 320.0, 200.0, 90.0, 15.0          # base tube: length, width (depth), height
CAN_W, CAN_D, CAN_H, CAN_R = 130.0, 66.0, 200.0, 65.0  # canopy inside: width, depth, side height, arch radius
CAN_V0 = 20.0                                       # canopy back sits 20 mm in from the base's back edge
DR_W, DR_D, DR_H = 194.0, 158.0, 86.0               # drawer outside
WHEEL_R = 50.0


# ------------------------------------------------------------- 1 base tube
def base_page():
    m = 30.0
    x0, y0 = m, m
    yb, yt, yf, ybo, yg = y0, y0 + BH, y0 + BH + BW, y0 + 2 * BH + BW, y0 + 2 * BH + 2 * BW
    b = []
    # --- artwork
    # back panel (upside down in the net): legend
    b.append(f'<g transform="translate({f(x0 + L)},{f(yt)}) rotate(180)">{legend_panel(L, BH)}</g>')
    # top panel: stage
    b.append(rect(x0, yt, L, BW, DEEP))
    for i in range(1, int(BW // 12)):
        b.append(line(x0, yt + i * 12, x0 + L, yt + i * 12, f'stroke="{KRAFT}" stroke-width="0.5"'))
    cx = x0 + L / 2
    b.append(rect(cx - CAN_W / 2, yt + CAN_V0, CAN_W, CAN_D, PAPER, f'stroke="{TERRA}" stroke-width="0.6" stroke-dasharray="2 1.5"'))
    b.append(text(cx, yt + CAN_V0 + CAN_D / 2 + 2, "The ratha canopy stands here", 4, TERRA, BODY, 600, "middle"))
    b.append(text(x0 + 8, yf - 6, "STAGE · push the pegs up through any two holes", 3.4, INK, BODY, 600, ls=0.4))
    # front panel: name band
    b.append(rect(x0, yf, L, BH, TERRA))
    b.append(lotus_band(x0, yf + BH - 24, L, 24, INDIGO, MARI))
    b.append(text(x0 + 10, yf + 11, "KATHA · A FOLK WITH FOLKS KIT", 4.2, PAPER, BODY, 600, ls=0.8))
    b.append(rect(x0 + L - 24, yf + 5, 15, 9, "none", f'stroke="{PAPER}" stroke-width="0.6" rx="1.5"'))
    b.append(text(x0 + L - 16.5, yf + 11.8, "7+", 5.5, PAPER, DISPLAY, 800, "middle"))
    b.append(text(cx, yf + 46, "Chanakya's Kit of <tspan fill='%s'>Wit</tspan>" % MARI, 19, PAPER, STORY, 650, "middle", True))
    b.append(text(cx, yf + 58, "Build him. Shoot him. Keep him.", 5.2, PAPER, DISPLAY, 800, "middle"))
    # bottom panel
    b.append(rect(x0, ybo, L, BW, INDIGO))
    b.append(coin(cx, ybo + 80, 34, PAPER, INK))
    b.append(text(cx, ybo + 120, "Katha 01 · Chanakya's Kit of Wit", 6, PAPER, STORY, 600, "middle", True))
    b.append(text(cx, ybo + 130, "folkwithfolks.in · made in Mumbai", 4, PAPER, BODY, 500, "middle"))
    # glue flap
    b.append(rect(x0 + 3, yg, L - 6, GLUEW, "none", GLUE))
    # --- dieline
    b.append(poly([(x0, yb), (x0 + L, yb), (x0 + L, yg), (x0 + L - 3, yg + GLUEW), (x0 + 3, yg + GLUEW), (x0, yg)]))
    for y in (yt, yf, ybo, yg):
        b.append(line(x0, y, x0 + L, y))
    # canopy lock slots
    for u in (cx - CAN_W / 2, cx + CAN_W / 2):
        for v0, v1 in ((12, 30), (36, 54)):
            b.append(rect(u - 0.8, yt + CAN_V0 + v0 - 0.5, 1.6, v1 - v0 + 1, "none", CUT))
    # peg holes (4.2 mm for 4 mm pegs; foot loops open 5 mm)
    for v in (110, 130, 150, 170):
        for u in range(30, 300, 20):
            b.append(circ(x0 + u, yt + v, 2.1, "none", CUT))
    b.append(text(x0 - 4, yt + BW / 2, "TOP", 4, INK, BODY, 700, "end"))
    for lab, y in (("BACK", yb + BH / 2), ("FRONT", yf + BH / 2), ("BOTTOM", ybo + BW / 2), ("GLUE", yg + 9)):
        b.append(text(x0 - 4, y, lab, 4, INK, BODY, 700, "end"))
    b.append(text(x0 + L + 6, yt + 10, "Ends stay open:", 3.6, INK, BODY, 600))
    b.append(text(x0 + L + 6, yt + 15, "a drawer slides in", 3.6))
    b.append(text(x0 + L + 6, yt + 20, "from each side.", 3.6))
    return page("page-2-base", "2 · Base tube · 320 × 200 × 90 · 400 gsm board, factory glued", L + 2 * m + 46, 2 * BH + 2 * BW + GLUEW + 2 * m + 18, b)


LEGEND = [
    ("lotus", "Lotus", ["Grows clean out of muddy water.", "Mauryan pillars rise from a lotus bell."]),
    ("arch", "Chaitya arch", ["The horseshoe doorway of Lomas Rishi", "cave, carved in Mauryan times."]),
    ("wheel", "Chariot wheel", ["Arthashastra: one wheel alone does not", "turn. Even a king needs helpers."]),
    ("coin", "Punch-marked coin", ["Mauryan silver money, stamped with", "signs like the sun."]),
    ("leaf", "Palm-leaf book", ["The Arthashastra survived on palm", "leaves and was found again in 1905."]),
    ("pillar", "Polished pillar", ["Mauryan stone was polished until", "it shone like glass."]),
]


def legend_icon(kind, cx, cy, s):
    if kind == "lotus":
        return lotus(cx, cy + s * .35, s * .7, TERRA)
    if kind == "arch":
        return poly(chaitya_pts(cx, cy + s * .45, cy - s * .05, s * .28, s * .32), f'fill="none" stroke="{TERRA}" stroke-width="{f(s * .09)}"', closed=False)
    if kind == "wheel":
        return wheel(cx, cy, s * .45, MARI, TERRA)
    if kind == "coin":
        return coin(cx, cy, s * .8, PAPER, INK)
    if kind == "leaf":
        return palmleaf(cx - s * .5, cy - s * .14, s, s * .28, MARI, INK)
    return pillar(cx - s * .08, cy - s * .48, s * .16, s * .95, TERRA, MARI)


def legend_panel(w, h):
    g = [rect(0, 0, w, h, INDIGO), text(10, 14, "What the symbols mean", 6.5, PAPER, DISPLAY, 800),
         text(10, 20.5, "Every pattern on this ratha comes from Chanakya's Mauryan world.", 3.2, PAPER, BODY, 400)]
    cw = (w - 20) / 3
    for i, (k, name, lines_) in enumerate(LEGEND):
        cxl, cyl = 10 + (i % 3) * cw, 27 + (i // 3) * 30
        g.append(rect(cxl, cyl, cw - 4, 27, PAPER, 'rx="2"'))
        g.append(legend_icon(k, cxl + 12, cyl + 13.5, 18))
        g.append(text(cxl + 24, cyl + 8, name, 3.8, TERRA, DISPLAY, 800))
        for j, ln in enumerate(lines_):
            g.append(text(cxl + 24, cyl + 14 + j * 4.4, ln, 3.05, INK, BODY, 400))
    return "".join(g)


# ------------------------------------------------------------- 3 drawers
def drawer_net(x0, y0, label, sub):
    """x0, y0 = top-left of the base panel."""
    b = []
    W, D, H = DR_W, DR_D, DR_H
    fy = y0 - H                    # front wall (outside face)
    iy = fy - (H - 2)              # inner fold-over
    by = y0 + D                    # back wall
    # artwork: front wall outside
    b.append(rect(x0, fy, W, H, TERRA))
    b.append(lotus_band(x0, fy + H - 18, W, 18, INDIGO, MARI))
    b.append(text(x0 + 7, fy + 9, label, 3.6, PAPER, BODY, 700, ls=0.5))
    b.append(text(x0 + 7, fy + 14, sub, 3.2, PAPER, BODY, 400))
    b.append(circ(x0 + W / 2, fy + H - 50, WHEEL_R, "none", f'stroke="{PAPER}" stroke-width="0.4" stroke-dasharray="1.5 1.5"'))
    b.append(text(x0 + W / 2, fy + H - 50 + 2, "wheel glued here", 3.2, PAPER, BODY, 500, "middle"))
    # unprinted kraft everywhere else
    for r_ in ((x0, y0, W, D), (x0, iy - 8, W, H - 2 + 8), (x0, by, W, H), (x0 - H, y0, H, D), (x0 + W, y0, H, D)):
        b.append(rect(*r_, KRAFT))
    b.append(text(x0 + W / 2, y0 + D / 2, "unprinted kraft inside", 3.4, INK, BODY, 500, "middle"))
    # dieline outline
    tabs = [(x0 + 40, x0 + 70), (x0 + W - 70, x0 + W - 40)]
    top = [(x0, fy), (x0, iy)]
    for a, c in tabs:
        top += [(a, iy), (a + 2, iy - 8), (c - 2, iy - 8), (c, iy)]
    top += [(x0 + W, iy), (x0 + W, fy)]
    # right side wall with corner glue flaps
    right = [(x0 + W, y0), (x0 + W + 2, y0 - 14), (x0 + W + H - 4, y0 - 14), (x0 + W + H, y0),
             (x0 + W + H, by - H + D), (x0 + W + H - 4, y0 + D + 14), (x0 + W + 2, y0 + D + 14), (x0 + W, y0 + D)]
    bottom = [(x0 + W, by), (x0 + W, by + H), (x0, by + H), (x0, by)]
    left = [(x0, y0 + D), (x0 - 2, y0 + D + 14), (x0 - H + 4, y0 + D + 14), (x0 - H, y0 + D), (x0 - H, y0),
            (x0 - H + 4, y0 - 14), (x0 - 2, y0 - 14), (x0, y0)]
    b.append(poly(top + right + bottom + left))
    for g_ in ((x0 + W + 2, y0 - 14, x0 + W + H - 4, 14), (x0 + W + 2, y0 + D, x0 + W + H - 4, 14),
               (x0 - H + 4, y0 - 14, x0 - 2, 14), (x0 - H + 4, y0 + D, x0 - 2, 14)):
        b.append(rect(g_[0], g_[1], g_[2] - g_[0], g_[3], "none", GLUE))
    b += [line(x0, y0, x0 + W, y0), line(x0, fy, x0 + W, fy), line(x0, by, x0 + W, by),
          line(x0, y0, x0, y0 + D), line(x0 + W, y0, x0 + W, y0 + D),
          line(x0 - H, y0, x0, y0), line(x0 - H, y0 + D, x0, y0 + D), line(x0 + W, y0, x0 + W + H, y0),
          line(x0 + W, y0 + D, x0 + W + H, y0 + D)]
    for a, c in tabs:
        b.append(line(a, iy, c, iy))
        b.append(rect(a + 1, y0 + 2, c - a - 2, 1.6, "none", CUT))     # lock slots in the base
    return b


def drawers_page():
    m = 30.0
    b = []
    y0 = m + 2 * DR_H + 8 + 14
    b += drawer_net(m + DR_H, y0, "DRAWER 1 · SKELETON + STENCILS", "Armature lies on the diagonal")
    b += drawer_net(m + 3 * DR_H + DR_W + 40, y0, "DRAWER 2 · CLAY + CLOTH", "Clay, shawl, tools, cards, plinth")
    w = 2 * (DR_W + 2 * DR_H) + 40 + 2 * m
    h = y0 + DR_D + DR_H + 14 + m + 18
    return page("page-3-drawers", "3 · Drawers ×2 · 194 × 158 × 86 · 400 gsm board, factory glued", w, h, b)


# ----------------------------------------------- 4 wheels, plinth, window
def small_parts_page():
    m = 30.0
    b = []
    R = WHEEL_R
    for i in range(2):
        cx = m + R + i * (2 * R + 12)
        b.append(wheel(cx, m + R, R, MARI, TERRA))
        b.append(circ(cx, m + R, R, "none", CUT))
        b.append(text(cx, m + 2 * R + 7, "wheel face", 3.6, INK, BODY, 600, "middle"))
        b.append(circ(cx, m + 3 * R + 18, R, KRAFT, CUT))
        b.append(text(cx, m + 3 * R + 20, "backer", 3.6, INK, BODY, 600, "middle"))
    for i in range(4):
        cx = m + 2 * (2 * R + 12) + 34 + (i % 2) * 66
        cy = m + 32 + (i // 2) * 66
        b.append(circ(cx, cy, 30, KRAFT, CUT))
        b.append(text(cx, cy + 1.5, "spacer", 3.4, INK, BODY, 600, "middle"))
    b.append(text(m, m + 4 * R + 32, "Each wheel: face + backer + 2 spacers, 1.5 mm greyboard, glued.",
                  3.8, INK, BODY, 400))
    b.append(text(m, m + 4 * R + 37.5, "The spacers lift the rim 3 mm off the drawer, so small fingers can pull it.", 3.8, INK, BODY, 400))
    # plinth: upside-down tray 50 × 50 × 15
    px, py, s, h = m + 30, m + 4 * R + 72, 50.0, 15.0
    b.append(rect(px, py, s, s, DEEP))
    b.append(lotus(px + s / 2, py + s - 8, 10, TERRA))
    for wx, wy, ww, wh in ((px, py - h, s, h), (px, py + s, s, h), (px - h, py, h, s), (px + s, py, h, s)):
        b.append(rect(wx, wy, ww, wh, INDIGO))
    outline = [(px, py - h), (px + s, py - h), (px + s, py), (px + s + h, py), (px + s + h, py + s), (px + s, py + s),
               (px + s, py + s + h), (px, py + s + h), (px, py + s), (px - h, py + s), (px - h, py), (px, py)]
    # corner glue flaps on the top/bottom walls
    for gx, gy, d in ((px, py - h, -1), (px + s, py - h, 1), (px, py + s, -1), (px + s, py + s, 1)):
        fl = [(gx, gy + 1), (gx + d * 9, gy + 3), (gx + d * 9, gy + h - 3), (gx, gy + h - 1)]
        b.append(poly(fl))
        b.append(fillpoly(fl, "#3B82F6", 'fill-opacity="0.18"'))
    b.append(poly(outline))
    for l_ in ((px, py, px + s, py), (px, py + s, px + s, py + s), (px, py, px, py + s), (px + s, py, px + s, py + s)):
        b.append(line(*l_))
    for dx in (-14, 14):
        b.append(circ(px + s / 2 + dx, py + s / 2 - 6, 2.1, "none", CUT))
    b.append(text(px + s / 2, py + s + h + 9, "Plinth 50 × 50 × 15", 3.8, INK, BODY, 600, "middle"))
    b.append(text(px + s / 2, py + s + h + 14, "pegs go up through the 2 holes", 3.4, INK, BODY, 400, "middle"))
    # PET window
    wx, wy = m + 150, m + 4 * R + 50
    win = [(wx, wy + 230)] + arc_pts(wx + 10, wy + 10, 10, 180, 90, 12) + arc_pts(wx + 100, wy + 10, 10, 90, 0, 12) + [(wx + 110, wy + 230)]
    b.append(fillpoly(win, "#DDEFF5"))
    b.append(poly(win))
    b.append(text(wx + 55, wy + 115, "Clear window", 4.2, INK, BODY, 700, "middle"))
    b.append(text(wx + 55, wy + 121, "110 × 230 · 0.5 mm PET", 3.6, INK, BODY, 400, "middle"))
    b.append(text(wx + 55, wy + 126, "slides out for filming", 3.6, INK, BODY, 400, "middle"))
    return page("page-4-wheels-plinth-window", "4 · Wheels, plinth and window", 330, wy + 230 + m + 18, b)


# ------------------------------------------------------------ 5 canopy
def canopy_geom():
    """Net in 'up' coordinates: x right, y up, y = 0 is the floor line. Columns:
    back 0–130 | side 1 130–196 | front 196–326 | side 2 326–392 | glue 392–407."""
    xb, xs1, xf, xs2, xg, xe = 0, CAN_W, CAN_W + CAN_D, 2 * CAN_W + CAN_D, 2 * CAN_W + 2 * CAN_D, 2 * CAN_W + 2 * CAN_D + 15
    return xb, xs1, xf, xs2, xg, xe


def gable(cx, y0, R, finial=True):
    """Semicircle gable top from right to left in up-coords, with a kalasha finial at the top."""
    fw = 8.0
    a = math.degrees(math.acos(fw / R))
    right = [(cx + R * math.cos(math.radians(t)), y0 + R * math.sin(math.radians(t))) for t in [a * i / 30 for i in range(31)]]
    left = [(cx + R * math.cos(math.radians(t)), y0 + R * math.sin(math.radians(t))) for t in [180 - a + a * i / 30 for i in range(31)]]
    top = y0 + R * math.sin(math.radians(a))
    fin = [(cx + 3, top + 5), (cx + 5, top + 9), (cx, top + 17), (cx - 5, top + 9), (cx - 3, top + 5)] if finial else []
    return right + fin + left


def canopy_outline():
    xb, xs1, xf, xs2, xg, xe = canopy_geom()
    H, R, D = CAN_H, CAN_R, CAN_D
    p = [(xb, 0), (xs1, 0)]
    for t0, t1 in ((12, 30), (36, 54)):                       # side 1 lock tabs
        p += [(xs1 + t0, 0), (xs1 + t0 + 1, -12), (xs1 + t1 - 1, -12), (xs1 + t1, 0)]
    # inner frame, hinged on the front floor line, hanging down
    ix0, ix1, ir = xf + 1, xs2 - 1, R - 1
    p += [(xf, 0), (ix0, 0)]
    for t0, t1 in ((60, 80), (140, 160)):
        p += [(ix0, -t0), (ix0 - 8, -t0 - 2), (ix0 - 8, -t1 + 2), (ix0, -t1)]
    p += [(ix0, -H)]
    p += [(xf + CAN_W / 2 + ir * math.cos(math.radians(180 + 180 * i / 48)), -H + ir * math.sin(math.radians(180 + 180 * i / 48))) for i in range(49)]
    for t0, t1 in ((140, 160), (60, 80)):
        p += [(ix1, -t1), (ix1 + 8, -t1 + 2), (ix1 + 8, -t0 - 2), (ix1, -t0)]
    p += [(ix1, 0), (xs2, 0)]
    for t0, t1 in ((12, 30), (36, 54)):                       # side 2 lock tabs
        p += [(xs2 + t0, 0), (xs2 + t0 + 1, -12), (xs2 + t1 - 1, -12), (xs2 + t1, 0)]
    p += [(xg, 0), (xe, 4), (xe, H - 4), (xg, H), (xs2, H)]
    p += gable(xf + CAN_W / 2, H, R)                          # front gable, right to left
    band = math.pi * R                                        # roof band follows the semicircle
    p += [(xs1 + D, H), (xs1 + D, H + band), (xs1 + D - 10, H + band), (xs1 + D - 10, H + band + 12),
          (xs1 + 10, H + band + 12), (xs1 + 10, H + band), (xs1, H + band), (xs1, H)]
    p += gable(xb + CAN_W / 2, H, R)                          # back gable
    p += [(xb, H), (xb, 0)]
    return p, band


def canopy_page(inside=False):
    xb, xs1, xf, xs2, xg, xe = canopy_geom()
    H, R, D = CAN_H, CAN_R, CAN_D
    outline, band = canopy_outline()
    m = 30.0
    X0 = m + 14
    Y0 = m + H + band + 12
    netw = xe + 14
    mir = (lambda x: X0 + netw - 14 - x) if inside else (lambda x: X0 + x)

    def P(x, y):
        return (mir(x), Y0 - y)

    def PP(seq):
        return [P(x, y) for x, y in seq]

    b = []
    win = chaitya_pts(xf + CAN_W / 2, -22, -170, 42, 47)      # in up-coords y is negated below
    win_up = [(x, -y) for x, y in win]
    gable_back = [(xb, 0), (xb + CAN_W, 0), (xb + CAN_W, H)] + gable(xb + CAN_W / 2, H, R) + [(xb, H)]
    gable_front = [(xf, 0), (xf + CAN_W, 0), (xf + CAN_W, H)] + gable(xf + CAN_W / 2, H, R) + [(xf, H)]
    if not inside:
        # back: indigo with a buti of lotuses and coins
        b.append(fillpoly(PP(gable_back), INDIGO))
        for i in range(4):
            for j in range(6):
                x, y = xb + 18 + i * 31 + (15 if j % 2 else 0), 22 + j * 32
                if x < xb + CAN_W - 10:
                    b.append(lotus(*P(x, y), 7, MARI))
        b.append(coin(*P(xb + CAN_W / 2, H + 32), 26, PAPER, INK))
        # side 1: the name
        b.append(rect(*P(xs1, H), D, H, PAPER))
        b.append(f'<g transform="translate({f(P(xs1 + D / 2 + 10, 0)[0])},{f(P(0, 18)[1])}) rotate(-90)">'
                 + text(0, 0, "Chanakya", 34, TERRA, STORY, 650, "start", True) + "</g>")
        b.append(palmleaf(*P(xs1 + 8, H - 8), D - 16, 13, MARI, INK))
        # front: frame with Mauryan pillars around a chaitya-arch window
        b.append(fillpoly(PP(gable_front), PAPER))
        b.append(lotus_band(*P(xf, 18), CAN_W, 18, INDIGO, MARI, 16))
        for px_ in (xf + 7, xf + CAN_W - 19):
            b.append(pillar(*P(px_, 190), 12, 172, TERRA, MARI))
        for off, col, sw in ((7, MARI, 2.2), (3.5, TERRA, 1.4)):
            ring = chaitya_pts(xf + CAN_W / 2, -22, -170, 42 + off, 47 + off)
            b.append(poly(PP([(x, -y) for x, y in ring]), f'fill="none" stroke="{col}" stroke-width="{sw}"', closed=False))
        b.append(wheel(*P(xf + CAN_W / 2, H + 50), 9, MARI, TERRA))
        # side 2: the story
        b.append(rect(*P(xs2, H), D, H, PAPER))
        sx, sy = P(xs2 + 6, H - 14)
        story = ["Chanakya was not", "a king, and not a", "warrior. With his", "brain he built an", "empire.",
                 "", "Over 2,300 years ago", "this teacher wrote", "the Arthashastra,", "a book on how to", "run a kingdom.",
                 "", "He helped young", "Chandragupta take", "the throne and start", "the Mauryan empire."]
        b.append(text(sx, sy, "Who was", 5, INK, DISPLAY, 800))
        b.append(text(sx, sy + 6, "Chanakya?", 5, TERRA, DISPLAY, 800))
        for i, ln in enumerate(story):
            b.append(text(sx, sy + 15 + i * 4.6, ln, 3.5, INK, BODY, 400))
        qy = sy + 15 + len(story) * 4.6 + 8
        for i, ln in enumerate(["“One wheel alone", "does not turn.”"]):
            b.append(text(sx, qy + i * 5.5, ln, 4.4, TERRA, STORY, 600, italic=True))
        b.append(text(sx, qy + 12, "Arthashastra 1.7", 3.2, INK, BODY, 600))
        b.append(wheel(*P(xs2 + D / 2, 22), 12, MARI, TERRA))
        # roof band: barrel-vault rafters of a chaitya hall
        b.append(rect(*P(xs1, H + band), D, band, TERRA))
        for i in range(1, int(band // 12) + 1):
            y = H + i * 12
            b.append(line(*P(xs1, y), *P(xs1 + D, y), f'stroke="{INK}" stroke-width="1.6"'))
            b.append(line(*P(xs1, y + 3), *P(xs1 + D, y + 3), f'stroke="{MARI}" stroke-width="0.5"'))
        # inner frame (its printed face looks into the canopy)
        ifr = [(xf + 1, 0), (xs2 - 1, 0), (xs2 - 1, -H)] + [(xf + CAN_W / 2 + (R - 1) * math.cos(math.radians(-180 * i / 48)), -H + (R - 1) * math.sin(math.radians(-180 * i / 48))) for i in range(49)] + [(xf + 1, -H)]
        b.append(fillpoly(PP(ifr), PAPER))
        b.append(text(*P(xf + CAN_W / 2, -250), "inner frame · folds up behind the window", 3.2, INK, BODY, 500, "middle"))
        for (x, y) in ((xs1 + 3, 0),):
            pass
        b.append(rect(*P(xg + 1.5, H - 4), 12, H - 8, "none", GLUE))
    else:
        # inside: the back wall is the stage backdrop seen through the window
        b.append(fillpoly(PP(gable_back), INDIGO))
        b.append(sun(*P(xb + CAN_W / 2, 232), 10, MARI))
        arch = chaitya_pts(xb + CAN_W / 2, -12, -150, 50, 56)
        b.append(poly(PP([(x, -y) for x, y in arch]), f'fill="none" stroke="{MARI}" stroke-width="1.6"', closed=False))
        for i in range(7):
            b.append(lotus(*P(xb + 12 + i * 18, 14), 9, MARI))
        b.append(text(*P(xb + CAN_W / 2, 110), "backdrop", 3.6, PAPER, BODY, 500, "middle"))
        b.append(text(mir(xf + CAN_W / 2), Y0 - H / 2, "inside: unprinted", 3.6, INK, BODY, 500, "middle"))
    # --- dieline
    b.append(poly(PP(outline)))
    b.append(poly(PP(win_up)))                                          # front window
    b.append(poly(PP([(x, -y) for x, y in win_up])))                    # matching window in the inner frame
    folds = [((xs1, 0), (xs1, H)), ((xf, 0), (xf, H)), ((xs2, 0), (xs2, H)), ((xg, 4), (xg, H - 4)),
             ((xf + 1, 0), (xs2 - 1, 0)), ((xs1, H), (xs1 + D, H)), ((xs1 + 10, H + band), (xs1 + D - 10, H + band))]
    for s in (xs1, xs2):
        folds += [((s + 12, 0), (s + 30, 0)), ((s + 36, 0), (s + 54, 0))]
    for a_, c_ in folds:
        b.append(line(*P(*a_), *P(*c_)))
    for i in range(1, int(band // 10)):
        b.append(line(*P(xs1, H + i * 10), *P(xs1 + D, H + i * 10), SCORE))
    # slits: inner-frame tabs (3 mm behind the front corners) and the roof-band tab
    for sx_ in (xf - 3, xs2 + 3):
        for t0, t1 in ((61, 79), (141, 159)):
            b.append(poly(PP([(sx_ - 0.6, t0), (sx_ + 0.6, t0), (sx_ + 0.6, t1), (sx_ - 0.6, t1)])))
    b.append(poly(PP([(xs2 + 9, H - 8.6), (xs2 + D - 9, H - 8.6), (xs2 + D - 9, H - 7.4), (xs2 + 9, H - 7.4)])))
    labels = [("BACK", xb + CAN_W / 2, -8), ("SIDE", xs1 + D / 2, -20), ("FRONT", xf + CAN_W / 2, 6), ("SIDE", xs2 + D / 2, -20),
              ("ROOF BAND", xs1 + D / 2, H + band - 20)]
    if not inside:
        for lab, x, y in labels:
            b.append(text(*P(x, y), lab, 3.6, INK if lab != "FRONT" else PAPER, BODY, 700, "middle"))
    w = netw + 2 * m + 28
    hgt = Y0 + H + R + 14 + m + 18
    if inside:
        return page("page-6-canopy-inside", "6 · Canopy · inside print (seen from the back of the sheet)", w, hgt, b)
    return page("page-5-canopy", "5 · Canopy · ships flat, child pops it open · 400 gsm", w, hgt, b)


# ------------------------------------------------------------ 7 belly band
def band_page():
    m = 30.0
    segs = [("bottom", BW), ("front", BH + 5), ("top", BW), ("back", BH + 5), ("overlap", 25)]
    BHH = 110.0
    x, y0 = m, m
    b = []
    xs = []
    for name, w in segs:
        xs.append((name, x, x + w))
        x += w
    total = x - m
    b.append(rect(m, y0, total - 25, BHH, PAPER))
    d = dict((n, (a, c)) for n, a, c in xs)
    # front face: read with the band on the box
    a, c = d["front"]
    face = [rect(0, 0, BHH, c - a, TERRA), text(BHH / 2, 16, "KATHA 01", 4, PAPER, BODY, 700, "middle", ls=1),
            text(BHH / 2, 34, "Chanakya's", 11, PAPER, STORY, 650, "middle", True),
            text(BHH / 2, 47, "Kit of <tspan fill='%s'>Wit</tspan>" % MARI, 11, PAPER, STORY, 650, "middle", True),
            text(BHH / 2, 60, "Build him. Shoot him. Keep him.", 4, PAPER, DISPLAY, 800, "middle"),
            rect(BHH / 2 - 8, 70, 16, 10, "none", f'stroke="{PAPER}" stroke-width="0.6" rx="1.5"'),
            text(BHH / 2, 77.5, "7+", 6, PAPER, DISPLAY, 800, "middle"), lotus(BHH / 2, 93, 7, MARI)]
    b.append(f'<g transform="translate({f(c)},{f(y0)}) rotate(90)">{"".join(face)}</g>')
    a, c = d["top"]
    face = [rect(0, 0, BHH, c - a, INDIGO), text(BHH / 2, 30, "Your ratha is inside,", 6, PAPER, DISPLAY, 800, "middle"),
            text(BHH / 2, 39, "folded flat.", 6, PAPER, DISPLAY, 800, "middle"),
            text(BHH / 2, 52, "Pop it open, curve the roof,", 4, PAPER, BODY, 500, "middle"),
            text(BHH / 2, 58, "tuck the tab. Done.", 4, PAPER, BODY, 500, "middle"),
            wheel(BHH / 2, 100, 22, MARI, TERRA), lotus(BHH / 2, 170, 9, MARI)]
    b.append(f'<g transform="translate({f(c)},{f(y0)}) rotate(90)">{"".join(face)}</g>')
    a, c = d["back"]
    cont = ["1 wire skeleton + spare wire", "3 clays: beige, brown, black", "3 press stencils + base plate",
            "scraper, foil, shawl", "plinth + 2 pegs · 8 shot cards", "phone stand · window · manual"]
    face = [rect(0, 0, BHH, c - a, PAPER), text(8, 10, "IN THE BOX", 3.6, TERRA, BODY, 700, ls=0.6)]
    for i, ln in enumerate(cont):
        face.append(text(8, 16 + i * 4.4, ln, 3.2, INK, BODY, 400))
    face += [text(8, 48, "⚠ WARNING: Small parts. Not for children under 3 years.", 2.9, INK, BODY, 700),
             text(8, 52.5, "Wire ends are capped. Keep the caps on.", 2.9, INK, BODY, 400),
             text(8, 58, "Folk with Folks · Mumbai, India · folkwithfolks.in", 2.9, INK, BODY, 400),
             text(8, 62.5, "MRP · manufacturer · batch: to be added", 2.9, TERRA, BODY, 600),
             rect(62, 66, 40, 26, "#ffffff", f'stroke="{INK}" stroke-width="0.3"'), text(82, 81, "barcode", 3, INK, BODY, 400, "middle"),
             rect(8, 66, 22, 22, "#ffffff", f'stroke="{INK}" stroke-width="0.3" stroke-dasharray="1.2 1"'),
             text(19, 78, "QR", 3, INK, BODY, 400, "middle")]
    b.append(f'<g transform="translate({f(a)},{f(y0 + BHH)}) rotate(-90)">{"".join(face)}</g>')
    a, c = d["overlap"]
    b.append(rect(a, y0 + 3, c - a, BHH - 6, "none", GLUE))
    # dieline
    b.append(poly([(m, y0), (a, y0), (c, y0 + 3), (c, y0 + BHH - 3), (a, y0 + BHH), (m, y0 + BHH)]))
    for n, a_, c_ in xs[1:]:
        b.append(line(a_, y0, a_, y0 + BHH))
    for n, a_, c_ in xs:
        b.append(text((a_ + c_) / 2, y0 + BHH + 7, n.upper(), 3.6, INK, BODY, 700, "middle"))
    b.append(text(m, y0 + BHH + 16, "The band holds the folded canopy, window and phone stand on top of the base. Tear it off and keep the box.",
                  3.8, INK, BODY, 400))
    return page("page-7-belly-band", "7 · Retail band · 110 mm wide · 157 gsm art paper", total + 2 * m, BHH + 2 * m + 36, b)


# ------------------------------------------------------------ 8 phone stand
def stand_page():
    src = os.path.join(ROOT, "katha", "assets", "kit", "insert-phone-stand.svg")
    with open(src) as fh:
        inner = fh.read().split(">", 1)[1].rsplit("</svg>", 1)[0]
    m = 30.0
    b = [f'<g transform="translate({f(m)},{f(m)})">{inner}</g>',
         text(m, m + 166 + 10, "3 mm greyboard, laser cut. Ships under the folded canopy, on top of the base.", 3.8, INK, BODY, 400)]
    return page("page-8-phone-stand", "8 · Phone stand · punch-out, no glue", 246 + 2 * m + 120, 166 + 2 * m + 32, b)


# ----------------------------------------------------------- 1 overview
def overview_page():
    W, H = 420.0, 297.0
    b = [text(20, 26, "Katha 01 · Chanakya ratha", 13, INK, DISPLAY, 800),
         text(20, 34, "Dieline set. Every page after this one is drawn at 1:1 in millimetres.", 4.2, INK, BODY, 400)]
    s = 0.5
    ox, oy = 30, 245                                                         # closed + displayed front view at 1:2
    b.append(text(ox, 52, "Front view · 1:2 · ready to display", 4.2, INK, BODY, 700))
    b.append(rect(ox, oy - BH * s, L * s, BH * s, TERRA))
    b.append(rect(ox, oy - 24 * s, L * s, 24 * s, INDIGO))
    for i in range(10):
        b.append(lotus(ox + 8 + i * 16, oy - 4.5, 5, MARI))
    b.append(text(ox + L * s / 2, oy - 26, "Chanakya's Kit of Wit", 7, PAPER, STORY, 650, "middle", True))
    for ex in (ox - 2, ox + L * s):
        b.append(rect(ex, oy - 2 * WHEEL_R * s, 2, 2 * WHEEL_R * s, MARI))
    cx = ox + L * s / 2
    can_base = oy - BH * s
    front = [(cx - CAN_W * s / 2, can_base), (cx + CAN_W * s / 2, can_base), (cx + CAN_W * s / 2, can_base - CAN_H * s)]
    front += [(cx + CAN_R * s * math.cos(math.radians(t)), can_base - CAN_H * s - CAN_R * s * math.sin(math.radians(t))) for t in range(0, 181, 6)]
    front += [(cx - CAN_W * s / 2, can_base - CAN_H * s)]
    b.append(fillpoly(front, PAPER, f'stroke="{INK}" stroke-width="0.4"'))
    win = chaitya_pts(cx, can_base - 22 * s, can_base - 170 * s, 42 * s, 47 * s)
    b.append(fillpoly(win, "#DDEFF5", f'stroke="{TERRA}" stroke-width="0.8"'))
    for px_ in (cx - CAN_W * s / 2 + 3.5, cx + CAN_W * s / 2 - 9.5):
        b.append(pillar(px_, can_base - 190 * s, 6, 86, TERRA, MARI))
    b.append(rect(cx - 12, can_base - 8, 24, 7.5, INDIGO))
    b.append(rect(cx - 1.5, can_base - 8 - 105, 3, 105, INK, 'opacity=".25"'))
    b.append(text(cx, can_base - 60, "puppet", 3.4, INK, BODY, 500, "middle"))
    b.append(text(ox, oy + 10, "Base 320 × 200 × 90 · canopy 130 × 66, 282 tall · total height about 37 cm", 3.6, INK, BODY, 400))
    # steps
    steps = [("1", "Tear the band", "Lift off the folded canopy, window and phone-stand sheet."),
             ("2", "Pull a wheel", "Each wheel is a drawer. Drawer 1: skeleton + stencils. Drawer 2: clay + cloth."),
             ("3", "Build Chanakya", "Follow the manual. Stand him on the plinth, pegs up into the foot loops."),
             ("4", "Pop the canopy", "Open the flat tube, curve the roof band, tuck its tab into the slit."),
             ("5", "Lock it on", "Fold the inner frame up, side tabs into the slits. Push the 4 floor tabs into the stage."),
             ("6", "Shoot, then keep", "Slide the window out to film. Slide it back in: the ratha is his display case.")]
    sx, sy = 205, 52
    b.append(text(sx, sy, "How it goes together · no glue, no scissors", 4.2, INK, BODY, 700))
    for i, (n, t, d) in enumerate(steps):
        y = sy + 10 + i * 17
        b.append(circ(sx + 5, y + 2, 5, TERRA))
        b.append(text(sx + 5, y + 4, n, 5, PAPER, DISPLAY, 800, "middle"))
        b.append(text(sx + 14, y + 2, t, 4.4, INK, DISPLAY, 800))
        b.append(text(sx + 14, y + 8, d, 3.4, INK, BODY, 400))
    # page list
    py = 170
    b.append(text(sx, py, "Pages", 4.2, INK, BODY, 700))
    for i, ln in enumerate(["2 · Base tube (stage on top, symbol legend on the back)", "3 · Drawers ×2", "4 · Wheels, plinth, window",
                            "5 · Canopy outside", "6 · Canopy inside (backdrop)", "7 · Retail band", "8 · Phone stand"]):
        b.append(text(sx, py + 7 + i * 5.2, ln, 3.6, INK, BODY, 400))
    b.append(text(sx, 222, "Not cut or tested yet. Check on the first prototype: slot fit for the real board,", 3.4, TERRA, BODY, 600))
    b.append(text(sx, 227, "roof-band curve, drawer slide, and that the clothed puppet clears the arch.", 3.4, TERRA, BODY, 600))
    return page("page-1-overview", "1 · Overview", W, H, b)


def build_pdf(pages):
    html = []
    tmp = os.path.join(OUT, "_tmp")
    os.makedirs(tmp, exist_ok=True)
    ff = (f"@font-face{{font-family:'{DISPLAY}';src:url('file://{FONTS}/BricolageGrotesque-VariableFont_opsz_wdth_wght.ttf')}}"
          f"@font-face{{font-family:'{STORY}';src:url('file://{FONTS}/Fraunces-VariableFont_SOFT_WONK_opsz_wght.ttf')}}"
          f"@font-face{{font-family:'{STORY}';font-style:italic;src:url('file://{FONTS}/Fraunces-Italic-VariableFont_SOFT_WONK_opsz_wght.ttf')}}"
          f"@font-face{{font-family:'{BODY}';src:url('file://{FONTS}/HankenGrotesk-VariableFont_wght.ttf')}}")
    js = ["const { chromium } = require('playwright');", "(async () => { const b = await chromium.launch(); const p = await b.newPage();"]
    outs = []
    for i, (svgp, w, h) in enumerate(pages):
        hp = os.path.join(tmp, f"p{i}.html")
        with open(svgp) as fh:
            svg = fh.read()
        with open(hp, "w") as fh:
            fh.write(f"<!doctype html><meta charset='utf-8'><style>{ff}@page{{size:{f(w)}mm {f(h)}mm;margin:0}}"
                     f"html,body{{margin:0}}svg{{display:block}}</style>{svg}")
        op = os.path.join(tmp, f"p{i}.pdf")
        outs.append(op)
        js.append(f"await p.goto('file://{hp}'); await p.evaluate(() => document.fonts.ready);"
                  f"await p.pdf({{path:'{op}', width:'{f(w)}mm', height:'{f(h)}mm', printBackground:true}});")
    js.append("await b.close(); })();")
    jp = os.path.join(tmp, "render.js")
    with open(jp, "w") as fh:
        fh.write("\n".join(js))
    subprocess.run(["node", jp], check=True)
    final = os.path.join(OUT, "Katha01-Ratha-Dieline.pdf")
    subprocess.run(["pdfunite", *outs, final], check=True)
    for fpath in os.listdir(tmp):
        os.remove(os.path.join(tmp, fpath))
    os.rmdir(tmp)
    print("wrote", final)


if __name__ == "__main__":
    pages = [overview_page(), base_page(), drawers_page(), small_parts_page(), canopy_page(), canopy_page(inside=True),
             band_page(), stand_page()]
    build_pdf(pages)

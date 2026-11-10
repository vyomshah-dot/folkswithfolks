#!/usr/bin/env python3
"""Mini-prototype version of the Katha 01 ratha dieline: every page at the same 35% scale on A4.

Run after tools/gen-ratha-dieline.py:  python3 tools/gen-ratha-a4.py
Out: katha/assets/kit/ratha/Katha01-Ratha-Dieline-A4-mini.pdf
"""
import importlib.util
import os
import re

HERE = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("ratha", os.path.join(HERE, "gen-ratha-dieline.py"))
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)

SCALE = 0.35
NAMES = ["page-1-overview", "page-2-base", "page-3-drawers", "page-4-wheels-plinth-window", "page-5-canopy",
         "page-6-canopy-inside", "page-7-belly-band", "page-8-phone-stand"]


def wrap(name, i):
    src = os.path.join(R.OUT, name + ".svg")
    with open(src) as fh:
        svg = fh.read()
    w, h = (float(v) for v in re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg).groups())
    inner = svg.split(">", 1)[1].rsplit("</svg>", 1)[0]
    s = SCALE if i else min(287 / w, 200 / h)          # the overview is not a dieline: fit it to the sheet
    land = w * s > 200 or w > h
    PW, PH = (297.0, 210.0) if land else (210.0, 297.0)
    ox, oy = (PW - w * s) / 2, (PH - 16 - h * s) / 2 + 4
    note = ("Mini prototype · every dieline page at 35% · print at 100% / actual size, no fit-to-page" if i
            else "Overview (not to scale)")
    body = [R.rect(0, 0, PW, PH, "#ffffff"),
            f'<g transform="translate({R.f(ox)},{R.f(oy)}) scale({R.f(s)})">{inner}</g>',
            R.text(8, PH - 6, note, 3, R.INK, R.BODY, 500)]
    if i:
        body += [R.rect(PW - 58, PH - 12, 50, 5, "none", f'stroke="{R.INK}" stroke-width="0.3"'),
                 R.text(PW - 33, PH - 8.4, "this bar = 50 mm", 2.6, R.INK, R.BODY, 500, "middle"),
                 R.text(PW - 60, PH - 8.4, "check:", 2.6, R.INK, R.BODY, 500, "end")]
    out = os.path.join(R.OUT, f"a4-{name}.svg")
    with open(out, "w") as fh:
        fh.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{R.f(PW)}mm" height="{R.f(PH)}mm" '
                 f'viewBox="0 0 {R.f(PW)} {R.f(PH)}">' + "".join(body) + "</svg>")
    return out, PW, PH


if __name__ == "__main__":
    pages = [wrap(n, i) for i, n in enumerate(NAMES)]
    final = os.path.join(R.OUT, "Katha01-Ratha-Dieline.pdf")
    keep = final + ".keep"
    os.replace(final, keep)
    R.build_pdf(pages)
    os.replace(final, os.path.join(R.OUT, "Katha01-Ratha-Dieline-A4-mini.pdf"))
    os.replace(keep, final)
    for p, _, _ in pages:
        os.remove(p)
    print("wrote Katha01-Ratha-Dieline-A4-mini.pdf")

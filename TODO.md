# TODO — Folk with Folks & Katha

A living implementation list. Two halves: **digital** (what lives in this repo or on
servers) and **physical** (what you make with paper, ink, cardboard, and a printer).

Statuses:
- **Now** — do next, blocking other work
- **Next** — queued, no blockers
- **Later** — deliberate, not yet
- **Decide** — needs a call from you, not work yet

Last touched: 2026-06-04.

---

## 🟢 Digital — repo + infra

### Now
- [ ] **Enable GitHub Pages with Actions as the source.**
      Repo → Settings → Pages → Source: "GitHub Actions". First deploy fires automatically.
- [ ] **Connect this repo to a Claude.ai Project.**
      claude.ai → New Project → name "Folk with Folks" → Project knowledge → Connect GitHub
      → pick `folkswithfolks`. That's the "auto-sync" half of the design ↔ chat loop.
- [ ] **Point DNS at GitHub Pages.**
      `CNAME www → vyomshah-dot.github.io` plus the four GitHub Pages A records on `@`.
      Then Settings → Pages → Custom domain → enter the value from `CNAME`, tick Enforce HTTPS.
- [ ] **Domain spelling — pick one and propagate.**
      `CNAME` currently says `www.folkwithfolks.in`; the repo and most docs say
      `folkswithfolks.in`. Pick the canonical one, then update README.md, site/README.md,
      and any other references. (If both domains exist and one redirects, document that too.)

### Next
- [ ] **Install GitHub CLI** (`winget install GitHub.cli`) so future repo work and PR
      reviews stay in the terminal. Not blocking.
- [ ] **Watch the first Action run** on the Actions tab. If the sync step fails, ping me.
- [ ] **Add a tiny dev script `tools/serve.ps1`** that runs `python -m http.server 8000`
      from `site/`. Saves typing.
- [ ] **Add a CONTRIBUTING.md** with the editing checklist already in README §5 (so
      collaborators don't have to read the whole README to know "edit tokens here, not there").

### Later
- [ ] **Set up Dependabot / Renovate** for the GitHub Actions versions (`actions/checkout@v4`
      etc. will need bumps eventually).
- [ ] **Add a `_redirects` file** if you ever migrate to Netlify; not relevant on Pages.

---

## 🟢 Digital — Folk with Folks (master brand)

### Now
- [ ] **Decide:** does FwF need a press-kit page (`/press`) on the live site, or is it
      private-share-only for now?

### Next
- [ ] **Studio page** on the live site — who you are, what you make, the YouTube channel
      slot. Reuse the website UI kit components in `folk-with-folks/ui_kits/website/`.
- [ ] **Slide-deck template** — `folk-with-folks/templates/deck-template.html`. README §9
      flags this as a deliberate gap.
- [ ] **Brand book v1.1** — fold in any tweaks from the past month into
      `folk-with-folks/brand-book.html` so it stays the authoritative source.

### Later
- [ ] **Email signature template** (HTML) using the wordmark and Hanken.
- [ ] **Letterhead** (PDF + HTML), folk divider at the top.

---

## 🟢 Digital — Katha (sub-brand)

### Now (all of these are TODOs flagged in `katha/README.md` §5)
- [ ] **`katha/assets/katha-logotype.svg`** — official vector for the Fraunces-italic
      terracotta logotype.
- [ ] **`katha/assets/badges/chanakya.svg`** — circular seal, sun motif, terracotta fill,
      "Chanakya · Kit of Wit" in Bricolage 800.
- [ ] **`katha/assets/badges/tenali.svg`** — diamond motif, marigold fill.
- [ ] **`katha/assets/badges/birbal.svg`** — neem-leaf motif, neem fill.

### Decide
- [ ] **Per-character accent overrides** — do Chanakya's web pages lean terracotta,
      Tenali's lean marigold, Birbal's lean neem? Or does the whole Katha world stay
      palette-balanced regardless of character? Affects the PDP and badge design.

### Next
- [ ] **Katha PDP — deploy it as a real route** on the live site (currently lives as a UI
      kit at `katha/ui_kits/pdp/`). Wire it to `/kits/chanakya-kit-of-wit`.
- [ ] **Katha storefront grid** — kit cards for all three characters, even if Tenali and
      Birbal show "Coming soon" badges.
- [ ] **`katha/voice.md`** — if Katha's voice needs more than the §3.5 paragraph in the
      README. Otherwise delete this TODO.

### Later
- [ ] **Katha Quest gamified dashboard** (XP, boss-stage, localStorage) — already mocked
      in `katha/chanakya-kit-of-wit-bible.html`. Port to a real route.
- [ ] **Tenali Kit bible** and **Birbal Kit bible** — parallel to the Chanakya one.

---

## 🟠 Physical — kit production

### Decide (these block everything downstream)
- [ ] **Material: outer sleeve** — paper-board weight (250 gsm? 300?), finish (matte,
      uncoated, with a soft texture). Affects emboss feasibility.
- [ ] **Material: inner tray** — corrugated or solid board. Affects strength.
- [ ] **Print method** — offset, digital, or screen. Offset is cheaper at >500 units;
      digital wins for the first prototype run.
- [ ] **Run size** — first prototype run: 1, 10, or 100 units? Drives printer choice.
- [ ] **Printer** — Mumbai-area printer who can emboss the torana arch.

### Now
- [ ] **CMYK conversion of the palette** — the brand colours are spec'd in RGB; print needs
      CMYK. Run them through a profile (FOGRA39 for India coated, ISO Uncoated for paper),
      log the CMYK values inside `brand-core/tokens.css` as comments next to each colour.
- [ ] **Bleed + safe-zone spec** for the outer sleeve dieline. 3mm bleed, 5mm safe zone.

### Next
- [ ] **Chanakya kit — outer sleeve dieline** (AI/PDF) with torana arch emboss area marked.
      Drop the source at `katha/assets/packaging/chanakya-sleeve.pdf` + `.ai`.
- [ ] **Chanakya kit — inner tray dieline.**
- [ ] **Instructions booklet** — A6, 8 pages, Hanken body 14px, sparse motifs. One spread
      per build step. Source at `katha/assets/packaging/chanakya-instructions.pdf`.
- [ ] **Safety card** — small parts ⚠ warning, the *one* sanctioned emoji.
- [ ] **FwF seal sticker** — 38mm circle, terracotta on paper, ink line.
- [ ] **Component spec sheet** — every cardboard piece, every dowel, every string. Saves
      arguments with the printer.

### Later
- [ ] **Prototype run** — 1 unit, hand-assembled, photographed for the PDP gallery.
- [ ] **Kid test** — give the prototype to a 7-year-old (not yours), watch them build it
      without help, note where the instructions failed.
- [ ] **Tenali kit packaging** — once Chanakya is locked.
- [ ] **Birbal kit packaging** — once Chanakya is locked.

---

## 🟠 Physical — launch & socials

### Decide
- [ ] **Launch date** for the Chanakya kit.
- [ ] **Pricing** — single SKU price for the first kit. Anchor the unit economics.

### Next
- [ ] **`@katha.by.vyom` content plan** — week 1 to week 4. Behind-the-build carousels,
      finished-puppet reels, one kid demo. Already sketched in `katha/README.md` §3.6.
- [ ] **Launch teaser** — 15-second reel, Fraunces italic title card, motif transition.
- [ ] **Press-release one-pager** — for whichever Indian craft / parenting publication
      you pitch first.

### Later
- [ ] **Workshop format** — could a Katha kit be a 90-minute paid workshop in a Mumbai
      bookstore or café? Material list, pricing, partner list.

---

## How to use this file

- Tick boxes as you finish things. Git history is your audit trail.
- New ideas go in as **Decide** items first; promote to **Now/Next/Later** once you've
  made the call.
- When you finish a phase (e.g. "Chanakya kit ships"), archive its checked items to
  `_archive/TODO-2026-Q3.md` so this list stays scannable.
